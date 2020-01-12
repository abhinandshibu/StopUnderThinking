from app import app, db
from flask import render_template, redirect, url_for, session
from flask_login import login_required, current_user, login_user, logout_user
from app.src.signup import signupValidation
from app.src.login import loginValidation
from app.src.user_tree import user_tree
from app.forms import LoginForm, SignupForm, NewJournal, NewEntry, NewSection, EntryInput
from app.models import User, Journal, Entry, Section
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
@app.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template('landing.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        error, user_id = signupValidation(form)
        if not error:
            # i.e. if no errors, send to journal landing
            session['user_id'] = user_id
            return redirect(url_for('journal_land'))
        else:
            return render_template('signup.html', form=form, error=error)
    else:
        return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        error, user_id = loginValidation(form)
        if not error:
            # i.e. if no errors, send to journal landing, pass user id to url_for
            session['user_id'] = user_id
            return redirect(url_for('journal_land'))
        else:
            return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)


@app.route('/signout', methods=['GET', 'POST'])
def signout():
    logout_user()
    return redirect('/landing')


@app.route('/journal_land', methods=['GET', 'POST'])
@login_required
def journal_land():
    # constructing the tree
    user_id = session['user_id']
    tree = user_tree(user_id)
    # number of journals
    journal_no = len(tree) - 1
    # form for new inputs of journals
    form = NewJournal()
    if form.validate_on_submit():

        journal = Journal(name=form.new_journal.data, user_id=user_id)
        db.session.add(journal)
        db.session.commit()

        section = Section(name="my section", journal_id=journal.id)
        db.session.add(section)
        db.session.commit()

        entry = Entry(name="my entry", section_id=section.id, content="this is some content")
        db.session.add(entry)
        db.session.commit()

        user_id = session['user_id']
        tree = user_tree(user_id)
        journal_no = len(tree) - 1
        form.new_journal.data = ''
        return render_template('journal-land.html', tree=tree, journal_no=journal_no, form=form, name=tree[0][1])
    return render_template('journal-land.html', tree=tree, journal_no=journal_no, form=form, name=tree[0][1])


@app.route('/journal-<journal_id>-<section_number>-<entry_number>/', methods=['GET', 'POST'])
@login_required
def journal(journal_id, section_number, entry_number):
    # journal_id is id in database, section_number counts from 1 upwards, entry_number counts from 0 upwards
    # to overcome the vulnerability, check if the journal belongs to them

    user_id = session['user_id']
    if Journal.query.filter_by(id=journal_id, user_id=user_id).scalar() is None:
        return redirect(url_for('journal_land'))

    # Could have called this data easily into lists using database, but this tree is better cause it allows the names
    # of all sections to be loaded at once to display, reducing delay

    # Creating the user tree
    user_id = session['user_id']
    tree = user_tree(user_id)

    # Finding the journal location in the tree
    journal_location = 1
    while int(journal_id) != tree[journal_location][0][0]:
        journal_location += 1

    # Finds content of specific journal, so more efficient and doesn't have to sort through everything
    journal_content = tree[journal_location]

    # so that we can make changes to the database
    journal = Journal.query.filter_by(id=journal_id).scalar()
    section = Section.query.filter_by(id=(journal_content[int(section_number)][0][0])).scalar()
    entry = Entry.query.filter_by(id=(journal_content[int(section_number)][int(entry_number) + 1][0])).scalar()

    # Form inputs for new section and new entry
    form_new_section = NewSection()
    form_new_entry = NewEntry()

    # The entry variables we are sending
    entry_text = entry.content
    print("entry content", entry_text)
    entry_title = entry.name
    entry_last_mod = str(entry.last_mod)[0:16]

    if form_new_section.validate_on_submit():
        section = Section(name=form_new_section.section_input.data, journal_id=journal_id)
        db.session.add(section)
        db.session.commit()

        entry = Entry(name="my page", section_id=section.id, content="")
        db.session.add(entry)
        db.session.commit()

        form_new_section.section_input.data = ''

        # updating last mod of journal
        journal.last_mod = datetime.utcnow()
        db.session.commit()

        return redirect(url_for('journal', journal_id=journal_id, section_number=1, entry_number=0))

    if form_new_entry.validate_on_submit():
        section_id = journal_content[int(section_number)][0][0]

        entry = Entry(name=form_new_entry.entry_input.data, section_id=section_id, content="")
        db.session.add(entry)
        db.session.commit()

        form_new_entry.entry_input.data = ''

        # updating last mod of journal and section
        journal.last_mod = datetime.utcnow()
        section.last_mod = datetime.utcnow()
        db.session.commit()

        return redirect(url_for('journal', journal_id=journal_id, section_number=section_number, entry_number=0))

    # Entry details form
    entry_details = EntryInput()
    if entry_details.validate_on_submit():
        entry.content = entry_details.entry_content.data
        entry.name = entry_details.entry_name.data
        db.session.commit()

        # updating last mod of journal, section and entry
        journal.last_mod = datetime.utcnow()
        section.last_mod = datetime.utcnow()
        entry.last_mod = datetime.utcnow()
        db.session.commit()

    # to display the data
    entry_details.entry_content.data = entry.content

    return render_template('journal.html', journal_content=journal_content, journal_id=int(journal_id),
                           section_number=int(section_number), entry_number=int(entry_number), entry_title=entry_title,
                           entry_text=entry_text, form_new_section=form_new_section,
                           form_new_entry=form_new_entry, entry_details=entry_details, entry_last_mod=entry_last_mod)


