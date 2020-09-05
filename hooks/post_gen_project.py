import subprocess
import venv


INSTALL_IMMEDIATELY = "{{ cookiecutter.install_immediately }}" == "yes"


def install_immediately():
    venv.create("venv", with_pip=True)
    subprocess.run(
        ". venv/bin/activate && pip install -r requirements-dev.txt",
        shell=True,
        check=True,
    )


if __name__ == '__main__' and INSTALL_IMMEDIATELY:
    install_immediately()
