from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from db_conf import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)

    comments = relationship("Comment", backref="post")

    def __repr__(self):
        return (
            f"<Post(id={self.id}, title='{self.title}',"
            f" content='{self.content[:50]}...')>"
        )
