import click
from lib.database import Session, Base, engine
from lib.models.player import Player
from lib.models.tournament import Tournament
from lib.models.match import Match

# Create all tables
Base.metadata.create_all(engine)

session = Session()

@click.group()
def cli():
    """Multiplayer Tournament Organizer CLI."""
    pass

@cli.command()
@click.argument('name')
def add_player(name):
    """Add a new player."""
    player = Player(name=name)
    session.add(player)
    session.commit()
    click.echo(f"Added player: {player}")

@cli.command()
def list_players():
    """List all players."""
    players = session.query(Player).all()
    for player in players:
        click.echo(player)

@cli.command()
@click.argument('name')
def create_tournament(name):
    """Create a new tournament."""
    tournament = Tournament(name=name)
    session.add(tournament)
    session.commit()
    click.echo(f"Created tournament: {tournament}")

@cli.command()
def list_tournaments():
    """List all tournaments."""
    tournaments = session.query(Tournament).all()
    for tournament in tournaments:
        click.echo(tournament)

@cli.command()
@click.argument('tournament_id', type=int)
@click.argument('player_id', type=int)
def add_match(tournament_id, player_id):
    """Add a player to a tournament match."""
    tournament = session.query(Tournament).get(tournament_id)
    player = session.query(Player).get(player_id)
    if not tournament:
        click.echo("Tournament not found.")
        return
    if not player:
        click.echo("Player not found.")
        return
    match = Match(tournament=tournament, player=player)
    session.add(match)
    session.commit()
    click.echo(f"Added match: {match}")

@cli.command()
def list_matches():
    """List all matches."""
    matches = session.query(Match).all()
    for match in matches:
        click.echo(match)
