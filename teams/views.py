from django.shortcuts import render
from django.http import JsonResponse
from .models import Team, Player
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.http import QueryDict
from django.views.generic import View

# Create your views here.
def index(request):
  return render(request, 'teams/index.html')

def teams(request):

  if request.method == 'GET':
    teams = Team.objects.all()
    teams_json = serializers.serialize('json', teams)
    return JsonResponse(teams_json, safe=False)
  elif request.method == 'POST':
    teamname = request.POST.get('name')
    teampoints = request.POST.get('points')
    teamposition = request.POST.get('position')
    teamwins = request.POST.get('wins')
    teamlosses = request.POST.get('losses')
    teamdescription = request.POST.get('description')
    team = Team(name=teamname, points=teampoints, position=teamposition, wins=teamwins, losses=teamlosses, description=teamdescription)
    team.save()
    return JsonResponse({'message':'successfully created team'}, safe=False)
    

def players(request):
  if request.method == 'GET':
    players = Player.objects.all()
    players_json = serializers.serialize('json', players)
    return JsonResponse(players_json, safe=False)
  elif request.method == 'POST':
    playername = request.POST.get('name')
    playerposition = request.POST.get('position')
    teamid = request.POST.get('teamId')
    team = Team.objects.get(pk=teamid)
    player = Player(name=playername, position=playerposition, team=team)
    player.save()
    return JsonResponse({'message':'successfully created player'}, safe=False)

def player(request, playerid):

  if request.method == 'DELETE':
    player = Player.objects.get(pk=playerid)
    player.delete()
    return JsonResponse({'message': 'successfully deleted'}, safe=False)
  elif request.method == 'GET':
    player = Player.objects.get(pk=playerid)

    # convert Player python object to JSON
    player_data = serializers.serialize('json', [player,])
    struct = json.loads(player_data)
    player_json = json.dumps(struct[0])

    return JsonResponse(player_json, safe=False)
  elif request.method == 'PUT':
    player = Player.objects.get(pk=playerid)
    body = QueryDict(request.body)
    player.name = body.get('name')
    player.position = body.get('position')
    team = Team.objects.get(pk=body.get('teamId'))
    player.team = team
    player.save()
    return JsonResponse({'message': 'successfully updated player'}, safe=False)

def team(request, teamid):
  if request.method == 'DELETE':
    team = Team.objects.get(pk=teamid)
    team.delete()
    return JsonResponse({'message': 'successfuly deleted'}, safe=False)
  elif request.method == 'GET':
    team = Team.objects.get(pk=teamid)

    # convert Team python object to JSON
    team_data = serializers.serialize('json', [team,])
    struct = json.loads(team_data)
    team_json = json.dumps(struct[0])
    
    return JsonResponse(team_json, safe=False)
  elif request.method == 'PUT':
    body = QueryDict(request.body)
    team = Team.objects.get(pk=teamid)
    team.name = body.get('name')
    team.points = body.get('points')
    team.wins = body.get('wins')
    team.losses = body.get('losses')
    team.description = body.get('description')
    team.save()
    return JsonResponse({'message': 'successfully updated'}, safe=False)





