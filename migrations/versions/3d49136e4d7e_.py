"""empty message

Revision ID: 3d49136e4d7e
Revises: fa85eac9b0b6
Create Date: 2023-1-13 17:46:40.863285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d49136e4d7e'
down_revision = 'fa85eac9b0b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('planet_id', sa.String(length=80), nullable=False))
        batch_op.drop_constraint('planet_first_name_key', type_='unique')
        batch_op.create_unique_constraint(None, ['planet_name'])
        batch_op.drop_column('first_name')
        batch_op.drop_column('last_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('first_name', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('planet_first_name_key', ['first_name'])
        batch_op.drop_column('planet_id')
        batch_op.drop_column('planet_name')

    op.drop_table('favorite_planet')
    # ### end Alembic commands ###
