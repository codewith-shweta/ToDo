import typer
from rich.console import Console
from rich.table import Table

console =Console()    #obj
app= typer.Typer()  #obj from Typer library


@app.command(short_help='Add items ')
def add(task : str, category:str): 
    typer.echo(f"adding {task}, {category}")    #print from typer library
    show()

@app.command(short_help="Delete items")
def delete(position:int):
    typer.echo(f"deleting{position}")
    show()
    

@app.command(short_help="Update items")
def update(position:int, task:str, category:str):
    typer.echo(f'Update {position}, {task}, {category}')
    show()

@app.command()
def complete(position:int, task:str, category:str):
    typer.echo('Done')
    show()

@app.command()  #helper 
def get_category_color(category):
    Colors={'ToDo': 'Red'}
    if category in Colors:
        return Colors[category]
    return 'white'
    show()

@app.command()
def show():
    tasks=[('Role', 'HR')]
    console.print(" [bold magental]ToDos's[/bold magental]")

    table = Table(show_header=True, header_style='bold blue')
    table.add_column('#', style='dim', width=7)
    table.add_column("ToDo", min_width=20)
    table.add_column("Category", max_width=20, justify='right')
    table.add_column("Done", min_width=12, justify='right')

    for num, task in enumerate(tasks , start=1):
        c = get_category_color(task[1])
        chance= 'Active' if True==1 else 'Inactive'
        table.add_row(str(num), task[0], f'[{c}], {task[1]} [/{c}]', chance)      
    console.print(table)

if __name__ == "__main__":
    app()
    
# run py main.py , --help, add --help 
# py main.py add "todo-list" "sports"
