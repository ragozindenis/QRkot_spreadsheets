from datetime import datetime

from app.models import CharityFundAbstractModel


def investing(
    target: CharityFundAbstractModel,
    sources: list[CharityFundAbstractModel],
) -> list[CharityFundAbstractModel]:
    changed = []
    for source in sources:
        invest_fund = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount
        )
        for obj in (target, source):
            obj.invested_amount += invest_fund
            if obj.invested_amount == obj.full_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()
        changed.append(source)
        if target.fully_invested:
            break
    return changed
