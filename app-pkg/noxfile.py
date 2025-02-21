from pathlib import Path

import nox


package_path = Path.cwd()
nox.options.default_venv_backend = 'uv'

def pip_sync(session, path):
    session.run('uv', 'pip', 'sync', path)


@nox.session
def tests(session: nox.Session):
    session.run('uv', 'sync', '--active', '--only-group', 'tests')
    session.run(
        'pytest',
        '-ra',
        '--tb=native',
        '--strict-markers',
        '--cov=mivepy',
        '--cov-config=.coveragerc',
        '--cov-report=xml',
        '--no-cov-on-fail',
        f'--junit-xml={package_path}/ci/test-reports/{session.name}.pytests.xml',
        'src/mivepy_tests',
        *session.posargs,
    )


@nox.session
def precommit(session: nox.Session):
    session.run('uv', 'sync', '--active', '--only-group', 'pre-commit')
    session.run(
        'pre-commit',
        'run',
        '--all-files',
    )


@nox.session
def audit(session: nox.Session):
    # Much faster to install the deps first and have pip-audit run against the venv
    session.run('uv', 'sync', '--active')
    session.run(
        'pip-audit',
        '--desc',
        '--skip-editable',
    )
