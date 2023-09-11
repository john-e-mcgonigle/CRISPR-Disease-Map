from typing import List

from sqlalchemy import Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import DetachedInstanceError

from crispr_disease_map import db

# class ScreenComparisons(DeclarativeBase):
#     __tablename__ = "comparison"


class Screen(db.Model):
    __tablename__ = "screen"

    id: Mapped[int] = mapped_column(primary_key=True)
    screen_name: Mapped[str]
    disease: Mapped[str]

    samples: Mapped[List["Sample"]] = relationship(
        back_populates="screen",
        primaryjoin="Screen.id==Sample.screen_id",
    )

    def __repr__(self):
        return self._repr(
            id=self.id,
            screen_name=self.screen_name,
            disease=self.disease,
        )


class Sample(db.Model):
    __tablename__ = "sample"

    id: Mapped[int] = mapped_column(primary_key=True)
    screen_id: Mapped["Screen"] = relationship(
        back_populates="samples",
        primaryjoin="Screen.id==Sample.screen_id",
    )
    cell_line: Mapped[str]
    gene_ko: Mapped[str]
    treatment: Mapped[str]
    dose: Mapped[str]
    days: Mapped[int]

    def __repr__(self):
        return self._repr(
            id=self.id,
            screen_id=self.screen_id,
            cell_line=self.cell_line,
            gene_ko=self.gene_ko,
            treatment=self.treatment,
            dose=self.dose,
            days=self.days
        )

