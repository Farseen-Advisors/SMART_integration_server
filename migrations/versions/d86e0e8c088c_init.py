"""init

Revision ID: d86e0e8c088c
Revises: 
Create Date: 2025-01-20 19:06:20.411614

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd86e0e8c088c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sessions',
    sa.Column('id', sa.String(length=1024), nullable=False),
    sa.Column('iss', sa.String(length=1024), nullable=False),
    sa.Column('token_endpoint', sa.String(length=1024), nullable=True),
    sa.Column('launch_token', sa.String(length=2048), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('endpoint_data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sessions')
    # ### end Alembic commands ###
