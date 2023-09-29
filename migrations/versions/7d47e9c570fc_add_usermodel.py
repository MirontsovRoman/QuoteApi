"""Add UserModel

Revision ID: 7d47e9c570fc
Revises: 1b7787ba33bb
Create Date: 2023-09-28 19:45:30.773895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d47e9c570fc'
down_revision = '1b7787ba33bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author_model', schema=None) as batch_op:
        batch_op.alter_column('surname',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)

    with op.batch_alter_table('quote_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), server_default='2', nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quote_model', schema=None) as batch_op:
        batch_op.drop_column('rating')

    with op.batch_alter_table('author_model', schema=None) as batch_op:
        batch_op.alter_column('surname',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)

    # ### end Alembic commands ###