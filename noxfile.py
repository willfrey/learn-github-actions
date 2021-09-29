from nox_poetry import session, Session


@session
def tests(session: Session) -> None:
    session.install(".", "pytest")
    session.run("pytest", *session.posargs)
