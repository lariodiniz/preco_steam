"""criando banco

Revision ID: 33d34d5ec22f
Revises: 
Create Date: 2022-08-04 12:58:57.537042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33d34d5ec22f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'jogos',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('link', sa.String(length=50), nullable=False),
        sa.Column('descricao', sa.String(length=250)),
        sa.Column('preco', sa.Integer())
    )
    op.create_table(
        'precos',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('jogo_id', sa.Integer(), sa.ForeignKey('jogos.id'), nullable=False),
        sa.Column('data', sa.DateTime(), nullable=False),
        sa.Column('valor', sa.Integer())
    )


def downgrade() -> None:
    op.drop_table('precos')
    op.drop_table('jogos')
