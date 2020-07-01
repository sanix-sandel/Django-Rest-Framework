from rest_framework import serializers
from games.models import GameCategory
from games.models import Game
from games.models import Player
from .models import PlayerScore
import games.views

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='game-detail'
    )

    class Meta:
        model=GameCategory
        fields=(
            'url',
            'pk',
            'name',
            'games'#from the related name with games
        )

#We use the games name that we
#specified as the related_name string value when 
#we created the game_category field as a
#models.ForeignKey instance in the Game model.


class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category=serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
        slug_field='name'    
    )#retrieve the game category's name instead of the id
    class Meta:
        model=Game
        fields=(
            'url',
            'game_category',
            'name',
            'related_date',
            'played',
        )


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    #Display all the details for the game
    game=GameSerializer()
    class Meta:
        model=PlayerScore
        fields=(
            'url',
            'pk',
            'score',
            'score_date',
            'game',
        )
#We don't include the 'player' field name in
#the fields tuple of string to avoid serializing the player again.
#         

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores=ScoreSerializer(many=True, read_only=True)
    gender=serializers.ChoiceField(
        choices=Player.GENDER_CHOICES
    )
    gender_description=serializers.CharField(
        source='get_gender_display',
        read_only=True
    )

    class Meta:
        model=Player
        fields=(
            'url',
            'name',
            'gender',
            'gender_description',
            'scores',
        )

#We use the scores name that we specified as the related_name string
#value when we created the player field as a models.ForeignKey 
#instance in the PlayerScore model.
# 
#         
class PlayerScoreSerializer(serializers.ModelSerializer):
    Player=serializers.SlugRelatedField(queryset=Player.objects.all(),
        slug_field='name'    
    )
    game=serializers.SlugRelatedField(queryset=Game.objects.all(), 
        slug_field='name'
    )

    class Meta:
        model=PlayerScore
        fields=(
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game',
        )