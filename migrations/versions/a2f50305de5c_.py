"""empty message

Revision ID: a2f50305de5c
Revises: cea5ea584b43
Create Date: 2019-11-10 12:54:11.721192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2f50305de5c'
down_revision = 'cea5ea584b43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('state', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'state')
    # ### end Alembic commands ###
