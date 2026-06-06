import json
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Media, UserMediaTrack, UserProfile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        nickname = request.POST.get('nickname')
        if form.is_valid() and nickname:
            if UserProfile.objects.filter(nickname=nickname).exists():
                form.add_error(None, 'Nickname already taken.')
            else:
                user = form.save()
                UserProfile.objects.create(user=user, nickname=nickname)
                login(request, user)
                return redirect('home')
        elif not nickname:
            form.add_error(None, 'Nickname is required.')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

@ensure_csrf_cookie
def home(request):
    watching_ids = []
    if request.user.is_authenticated:
        watching_ids = list(UserMediaTrack.objects.filter(user=request.user, status='Currently Watching').values_list('media__tvmaze_id', flat=True))
        
    return render(request, 'tracker/home.html', {'watching_ids': watching_ids})

@login_required
def public_profile(request, nickname=None):
    if not nickname:
        user_prof, _ = UserProfile.objects.get_or_create(user=request.user)
        if not user_prof.nickname:
            user_prof.nickname = f"user_{request.user.id}"
            user_prof.save()
        return redirect(f'/u/{user_prof.nickname}/')
        
    target_prof = get_object_or_404(UserProfile, nickname=nickname)
    is_owner = (target_prof.user == request.user)
    
    tracks = UserMediaTrack.objects.filter(user=target_prof.user).select_related('media')
    watching = tracks.filter(status='Currently Watching')
    watched = tracks.filter(status='Watched')
    planned = tracks.filter(status='Plan to Watch')
    dropped = tracks.filter(status='Dropped')
    
    is_following = target_prof.followers.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    
    followers_users = target_prof.followers.select_related('profile').all()
    followers_profiles = [u.profile for u in followers_users if hasattr(u, 'profile')]
    following_profiles = target_prof.user.following.all()
    
    return render(request, 'tracker/profile.html', {
        'watching': watching, 
        'watched': watched, 
        'planned': planned, 
        'dropped': dropped,
        'user_profile': target_prof,
        'is_owner': is_owner,
        'is_following': is_following,
        'followers_profiles': followers_profiles,
        'following_profiles': following_profiles
    })

@login_required
def add_to_list(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tvmaze_id = data.get('id')
        title = data.get('title')
        poster = data.get('poster')
        summary = data.get('summary', '')
        status = data.get('status')
        
        media, _ = Media.objects.get_or_create(
            tvmaze_id=tvmaze_id,
            defaults={'title': title, 'poster_url': poster, 'summary': summary}
        )
        
        if status == 'Remove':
            UserMediaTrack.objects.filter(user=request.user, media=media).delete()
            return JsonResponse({'success': True, 'removed': True})
            
        track, _ = UserMediaTrack.objects.get_or_create(user=request.user, media=media)
        track.status = status
        track.save()
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@login_required
def get_status(request):
    tvmaze_id = request.GET.get('id')
    if tvmaze_id:
        track = UserMediaTrack.objects.filter(user=request.user, media__tvmaze_id=tvmaze_id).first()
        if track:
            return JsonResponse({'status': track.status})
    return JsonResponse({'status': None})

@login_required
def upload_picture(request):
    if request.method == 'POST' and request.FILES.get('picture'):
        user_prof, _ = UserProfile.objects.get_or_create(user=request.user)
        user_prof.profile_picture = request.FILES['picture']
        user_prof.save()
        return JsonResponse({'success': True, 'url': user_prof.profile_picture.url})
    return JsonResponse({'success': False}, status=400)

@login_required
def follow_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nickname = data.get('nickname')
        target_prof = get_object_or_404(UserProfile, nickname=nickname)
        if target_prof.user == request.user:
            return JsonResponse({'success': False, 'error': 'Cannot follow yourself'})
            
        if target_prof.followers.filter(id=request.user.id).exists():
            target_prof.followers.remove(request.user)
            followed = False
        else:
            target_prof.followers.add(request.user)
            followed = True
            
        return JsonResponse({'success': True, 'followed': followed, 'count': target_prof.followers.count()})
    return JsonResponse({'success': False}, status=400)
