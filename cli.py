import json_manager
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', required=True, help='The name of the user.')
@click.option('--lastname', required=True, help='The lastname of the user.')
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail('Name and lastname are required')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_user = {
            "id": new_id,
            "name": name,
            "lastname": lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(
            f"User \"{name} - {lastname}\" created successfully with id {new_id}")


@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((item for item in data if item["id"] == int(id)), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        print(f"User: {user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((item for item in data if item["id"] == int(id)), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User with id {id} deleted successfully")


@cli.command()
@click.argument('id', type=int)
@click.option('--name', help='The name of the user.')
@click.option('--lastname', help='The lastname of the user.')
@click.pass_context
def update(ctx, id, name, lastname):
    data = json_manager.read_json()
    user = next((item for item in data if item["id"] == int(id)), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        if name is not None:
            user['name'] = name

        if lastname is not None:
            user['lastname'] = lastname

        if name is None and lastname is None:
            ctx.fail('Name or lastname is required')
        json_manager.write_json(data)
        print(f"User with id {id} updated successfully")


if __name__ == "__main__":
    cli()
