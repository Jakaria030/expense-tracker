
class Expense:
    def __init__(self, id, date, category, amount, currency, note, created_at):
        self.id = id
        self.date = date
        self.category = category
        self.amount = amount
        self.currency = currency
        self.note = note
        self.created_at = created_at
    
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "currency": self.currency,
            "note": self.note,
            "created_at": self.created_at
        }
