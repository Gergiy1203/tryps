from sqlalchemy.orm import Session
import models

def create_client(db: Session, client):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_clients(db: Session):
    return db.query(models.Client).all()


def create_task(db: Session, task):
    db_task = models.Task(**task.dict(), status="todo")
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session):
    return db.query(models.Task).all()
