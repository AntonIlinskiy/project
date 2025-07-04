"""create wallets table"""

from alembic import op
import sqlalchemy as sa

# Обязательные переменные:
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'wallets',
        sa.Column('uuid', sa.String, primary_key=True, index=True),
        sa.Column('balance', sa.Numeric(scale=2), nullable=False),
    )


def downgrade():
    op.drop_table('wallets')
