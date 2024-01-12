"""create tables

Revision ID: ebcc070c74c4
Revises: e5977731dd8a
Create Date: 2024-01-12 18:39:45.174126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebcc070c74c4'
down_revision = 'e5977731dd8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('contact', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('contact', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('clients_id', sa.Integer(), nullable=True),
    sa.Column('employees_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['clients_id'], ['clients.id'], name=op.f('fk_cars_clients_id_clients')),
    sa.ForeignKeyConstraint(['employees_id'], ['employees.id'], name=op.f('fk_cars_employees_id_employees')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    op.drop_table('employees')
    op.drop_table('clients')
    # ### end Alembic commands ###