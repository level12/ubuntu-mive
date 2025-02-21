from pathlib import Path

import nox


package_path = Path.cwd()
nox.options.default_venv_backend = 'uv'


def pip_sync(session, path):
    session.run('uv', 'pip', 'sync', path)


@nox.session
def tests(session: nox.Session):
    session.run('uv', 'sync', '--active', '--no-dev', '--group', 'tests')
    session.run(
        'pytest',
        '-ra',
        '--tb=native',
        '--strict-markers',
        'src/mivepy_tests',
        *session.posargs,
    )
