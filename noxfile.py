import nox


@nox.session(python=["3.8", "3.9"])
def install(session: nox.Session) -> None:
    session.run("
