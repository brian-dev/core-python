import git
import typer
import yaml

from PyInquirer import prompt
from rich import print as rprint

app = typer.Typer()


def load_repo_file(repo_name):
    with open(f'yaml_files/repos.yaml') as file_read:
        test_repo = yaml.safe_load(file_read)
    return test_repo[repo_name]


def clone_repo(target_repo):
    clone_target = load_repo_file(target_repo)
    git.Repo.clone_from(clone_target['ssh_url'], clone_target['repo_project_name'])


@app.command("clone_repo")
def sample_func():
    module_list_question = [
        {
            'type': 'list',
            'name': 'target_repo',
            'message': 'Select a project repository: ',
            'choices': [
                        {
                            'name': 'Notes API',
                        },
                        {
                            'name': 'Notes UI Behave',
                        },
                        {
                            'name': 'example_2',
                        },
                        {
                            'name': 'example_3',
                        },
            ],
        }
    ]

    target_repo = prompt(module_list_question)
    target_name = target_repo['target_repo'].replace(' ', '_').lower()
    clone_repo(target_name)

    rprint("[yellow]=============================================[yello]")
    rprint('[green bold]Success![green bold]')
    rprint(f"[green]{target_repo['target_repo']} was successfully cloned.[green]")


if __name__ == "__main__":
    app()
