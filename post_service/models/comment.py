from sqlalchemy import Column, ForeignKey, Integer, String, Text

from db_conf import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)

    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    def __repr__(self):
        return (
            f"<Comment(id={self.id}, title='{self.title}',"
            f" content='{self.content[:50]}...')>"
        )
