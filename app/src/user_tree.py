from app.models import User, Journal, Section, Entry
from sqlalchemy import desc


def user_tree(user_id):
    # quite hard to get your head round because of the layers of iteration
    # triple nested for loop
    tree = []

    user = User.query.filter_by(id=user_id).first()
    tree.append([user.id, user.firstname])

    journals = Journal.query.filter_by(user_id=user_id).order_by(desc(Journal.last_mod)).all()
    for journal_no in range(len(journals)):
        current_journal = journals[journal_no]
        temp_journal = [[current_journal.id, current_journal.name, current_journal.last_mod]]

        sections = Section.query.filter_by(journal_id=current_journal.id).order_by(desc(Section.last_mod)).all()
        for section_no in range(len(sections)):
            current_section = sections[section_no]
            temp_section = [[current_section.id, current_section.name, current_section.last_mod]]

            entries = Entry.query.filter_by(section_id=current_section.id).order_by(desc(Entry.last_mod)).all()
            for entry_no in range(len(entries)):
                current_entry = entries[entry_no]
                temp_section.append([current_entry.id, current_entry.name, current_entry.last_mod])

            temp_journal.append(temp_section)
        tree.append(temp_journal)

    return tree
