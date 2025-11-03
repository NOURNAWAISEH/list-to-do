from sqlalchemy import MetaData, Table, Column, Integer, String, Datetime,ENUM

class Status(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    deleted = "deleted"



user= Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False),
    Column("email", String(100), unique=True),
    Column("password", String(100), unique=True),
    Column("created_at", Datetime),
    Column("updated_at", Datetime)
)


sub-todo= Table(
    "sub-todo", metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50), nullable=False),
    Column("description", String(100), unique=True),
    Column("datetime", Datetime),
    Column("created_at", Datetime),
    Column("updated_at", Datetime),
    Column(
        Enum(Status),
        default=Status.pending, 
        nullable=False
    )
)

todo= Table(
    "todo", metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50), nullable=False),
    Column("description", String(100), unique=True),
    Column("datetime", Datetime),
    Column("created_at", Datetime),
    Column("updated_at", Datetime),
    Column(
        Enum(Status),
        default=Status.pending, 
        nullable=False
    )
    
)





