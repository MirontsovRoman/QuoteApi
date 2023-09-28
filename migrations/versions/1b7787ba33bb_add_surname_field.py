"""Add surname field

Revision ID: 1b7787ba33bb
Revises: f6eda7049057
Create Date: 2023-09-27 21:13:58.742019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b7787ba33bb'
down_revision = 'f6eda7049057'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('surname', sa.String(length=32), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author_model', schema=None) as batch_op:
        batch_op.drop_column('surname')

    # ### end Alembic commands ###