## ============================================================================
## ACT 6 DIALOGUES — Student Orgs & Campus Life
## KEY THEME: Organizations, extracurriculars, campus events, scholarships
## ============================================================================

## --- ACT 6 INIT ---
label act6_start:
    $ talked_mika = False
    $ talked_kuya_tomas = False
    $ talked_ate_jenny = False
    $ talked_coach_ramon = False
    jump act6_map

## ============================================================================
## NPC 1 — MIKA (Org Recruiter / Upperclassman)
## KEY INFO: Student organizations, how to join, what they offer
## ============================================================================
label act6_npc_mika:
    window show
    mika "Hey, freshie! Have you checked out the org fair yet?"
    player_char "Org fair? What's that?"
    mika "Oh, you're in for a treat! I'm Mika, president of the UPV Ecological Society."
    mika "Every start of semester, student organizations set up booths to recruit new members."
    mika "It's like a buffet of campus life — pick what interests you!"
    menu:
        "What kinds of orgs are there?":
            jump act6_mika_types
        "How do I join an org?":
            jump act6_mika_join
        "Is it worth joining an org as a freshie?":
            jump act6_mika_worth

label act6_mika_types:
    mika "UPV has a lot of recognized student organizations. Let me break them down."
    mika "Academic orgs — tied to your degree program. CFOS has marine science clubs, CAS has literary societies, CM has econ circles."
    mika "Socio-civic orgs — community service, outreach, volunteer work. Great for character building."
    mika "Cultural orgs — theater, dance, music, visual arts. UPV has a strong cultural scene."
    mika "Sports clubs — basketball, volleyball, swimming, martial arts. Some compete in inter-UP games."
    mika "Environmental orgs — like ours! Coastal cleanups, mangrove planting, marine conservation."
    mika "Publication orgs — the campus newspaper, literary journal, online media. If you like writing."
    mika "Religious orgs — various faith-based groups that hold fellowship and service activities."
    player_char "That's a lot of choices."
    mika "It is! My advice — join one or two max in your first semester. Don't overextend."
    menu:
        "How do I join?":
            jump act6_mika_join
        "Is it worth it as a freshie?":
            jump act6_mika_worth
        "(Thanks, Mika!)":
            jump act6_mika_end

label act6_mika_join:
    mika "Joining is simple. Here's the process:"
    mika "Step 1 — Attend the org fair or reach out to the org directly. Most have Facebook pages or group chats."
    mika "Step 2 — Sign up for their application process. Some orgs have interviews, others just require attendance at events."
    mika "Step 3 — Complete the membership requirements. This varies — it could be attending a seminar, a retreat, or working on a project."
    mika "Step 4 — Once accepted, pay the membership fee — usually ₱50 to ₱200 per semester."
    mika "Important: ALL recognized orgs must be registered with the OSA. If an org isn't OSA-registered, be careful."
    mika "Unregistered groups can't use campus facilities or organize official events."
    player_char "What if I want to start my own org?"
    mika "You can! You need at least 15 members, a constitution, a faculty adviser, and OSA approval."
    mika "It's a process, but the OSA staff are helpful. Ate Jenny there can walk you through it."
    menu:
        "Is it worth it as a freshie?":
            jump act6_mika_worth
        "(That's really helpful.)":
            jump act6_mika_end

label act6_mika_worth:
    mika "Absolutely worth it. Here's why."
    mika "One — community. You'll find your people. UP can feel isolating at first, especially in Miagao."
    mika "Two — skills. Leadership, event management, teamwork. These look great on your resume."
    mika "Three — connections. Upperclassmen in your org know which professors to take, which subjects to avoid."
    mika "Four — mental health. Having friends and a support system makes the UP experience survivable."
    mika "Five — some orgs offer academic support — reviewers, tutoring, shared notes."
    player_char "You make a strong case."
    mika "UP isn't just about grades. The best students are the ones who are involved."
    jump act6_mika_end

label act6_mika_end:
    mika "Come check out the EcoSoc booth if you're interested! We're the ones with the turtle banner."
    mika "And don't forget — org fair is only this week. Don't miss it!"
    $ talked_mika = True
    $ complete_task("talk_mika")
    window hide
    return

## ============================================================================
## NPC 2 — KUYA TOMAS (Scholarship Office Staff)
## KEY INFO: Scholarships, financial aid, stipends
## ============================================================================
label act6_npc_kuya_tomas:
    window show
    kuya_tomas "Good morning. Are you here for scholarship inquiries?"
    player_char "Yes, Kuya. I want to know what financial aid is available."
    kuya_tomas "Smart move coming early. A lot of freshmen don't find out about these until second semester."
    menu:
        "What scholarships are available?":
            jump act6_tomas_scholarships
        "How do I apply for financial aid?":
            jump act6_tomas_apply
        "What about the Socialized Tuition and Financial Assistance Program?":
            jump act6_tomas_stfap

label act6_tomas_scholarships:
    kuya_tomas "There are several types of scholarships available to UPV students:"
    kuya_tomas "University Scholarship — automatic for students with a GWA of 1.20 or better. Full tuition covered."
    kuya_tomas "College Scholarship — GWA of 1.45 or better. Partial or full tuition depending on the college."
    kuya_tomas "DOST Scholarship — from the Department of Science and Technology. For STEM students. Includes stipend and tuition."
    kuya_tomas "CHED Merit Scholarship — based on board exam entrance scores. Full tuition and monthly allowance."
    kuya_tomas "Private scholarships — various foundations offer them. Check the OSA bulletin board regularly."
    kuya_tomas "Barangay and LGU scholarships — some local government units offer educational assistance. Check with your home LGU."
    player_char "Are there scholarships specifically for UPV?"
    kuya_tomas "Yes — the UPV Foundation scholarships. These are donor-funded and have specific criteria."
    kuya_tomas "Some are need-based, others are merit-based. Applications open every start of semester."
    menu:
        "How do I apply?":
            jump act6_tomas_apply
        "What about STFAP?":
            jump act6_tomas_stfap
        "(That's very helpful.)":
            jump act6_tomas_end

label act6_tomas_apply:
    kuya_tomas "For university and college scholarships — these are automatic based on your grades. No application needed."
    kuya_tomas "For external scholarships like DOST or CHED — you should have applied before enrollment. If you missed it, apply next cycle."
    kuya_tomas "For UPV Foundation scholarships — get the application form from the OSA or the UPV Foundation office."
    kuya_tomas "Requirements usually include: grades transcript, certificate of income, essay, and recommendation letters."
    kuya_tomas "Deadlines are STRICT. Missing the deadline by even one day means disqualification."
    kuya_tomas "My advice — keep a folder with all your documents ready. Updated grades, income certificate, IDs."
    kuya_tomas "When scholarship season comes, you just grab the folder and go. No scrambling."
    player_char "What if I lose my scholarship?"
    kuya_tomas "Most scholarships have maintaining requirements — usually a minimum GWA."
    kuya_tomas "If you fall below, you get one semester of probation. If you don't recover, the scholarship is revoked."
    kuya_tomas "But you can always reapply once your grades improve."
    menu:
        "What about STFAP?":
            jump act6_tomas_stfap
        "(Thank you, Kuya.)":
            jump act6_tomas_end

label act6_tomas_stfap:
    kuya_tomas "STFAP — Socialized Tuition and Financial Assistance Program. This is a big one."
    kuya_tomas "It's UP's system for making education affordable based on your family's income."
    kuya_tomas "You're assigned a bracket from A to E9. Bracket A pays the highest tuition. Bracket E pays nothing — free tuition."
    kuya_tomas "Most students from low-income families fall into Brackets D or E."
    kuya_tomas "To apply, you need to submit an STFAP application form, your family's income tax return, and other financial documents."
    kuya_tomas "An interview may be conducted to verify your family's situation."
    kuya_tomas "IMPORTANT — if you don't apply for STFAP, you're automatically placed in the highest-paying bracket."
    kuya_tomas "So always apply, even if you think you don't qualify. The worst they can say is you stay in your current bracket."
    player_char "When is the STFAP application period?"
    kuya_tomas "Usually during the first two weeks of the semester. Watch for announcements from the Cashier's Office."
    kuya_tomas "The OSA can also help you with the paperwork. Don't be shy about asking."
    jump act6_tomas_end

label act6_tomas_end:
    kuya_tomas "Education is a right, not a privilege. UP believes that. Use every resource available to you."
    kuya_tomas "My office is right here in BOX 1, ground floor. Come back anytime."
    $ talked_kuya_tomas = True
    $ complete_task("talk_kuya_tomas")
    window hide
    return

## ============================================================================
## NPC 3 — ATE JENNY (OSA Staff)
## KEY INFO: Campus events, org registration, student handbook
## ============================================================================
label act6_npc_ate_jenny:
    window show
    ate_jenny "Hi! Welcome to the Office of Student Affairs. How can I help you?"
    player_char "Hi, Ate. I want to know more about campus events and what the OSA does."
    ate_jenny "Great question! The OSA is basically the hub of student life outside the classroom."
    menu:
        "What events happen on campus?":
            jump act6_jenny_events
        "What does the OSA handle?":
            jump act6_jenny_osa
        "Where can I find the Student Handbook?":
            jump act6_jenny_handbook

label act6_jenny_events:
    ate_jenny "UPV has a packed events calendar! Here are the major ones:"
    ate_jenny "Freshie Week — orientation activities, campus tours, and the org fair. That's happening right now!"
    ate_jenny "Lantern Parade — before Christmas break. Students and orgs build giant lanterns and parade them around campus."
    ate_jenny "Pahampang — the annual sports festival. Inter-college competitions in basketball, volleyball, swimming, and more."
    ate_jenny "Arts Month — cultural performances, art exhibits, literary readings. Usually March."
    ate_jenny "Loyalty Day — anniversary celebration of UPV. Guest speakers, awards, and a big program."
    ate_jenny "Graduation — the biggest event. Families flood Miagao. It's emotional and beautiful."
    player_char "Are freshmen allowed to participate in all of these?"
    ate_jenny "Absolutely! In fact, we encourage it. The more involved you are, the richer your UP experience."
    menu:
        "What does the OSA handle?":
            jump act6_jenny_osa
        "Where's the Student Handbook?":
            jump act6_jenny_handbook
        "(Sounds exciting!)":
            jump act6_jenny_end

label act6_jenny_osa:
    ate_jenny "The OSA handles a lot. Let me list the main ones:"
    ate_jenny "Student organization registration — all orgs must register with us every semester."
    ate_jenny "Scholarship processing and verification — we work with the Cashier's Office on this."
    ate_jenny "Student discipline — cases of misconduct, harassment, and violations go through us."
    ate_jenny "Counseling services — we have a guidance counselor on staff. Confidential and free."
    ate_jenny "Event permits — any org or student body event on campus needs OSA clearance."
    ate_jenny "Student welfare — dormitory concerns, emergency assistance, and student aid."
    player_char "You do counseling too?"
    ate_jenny "Yes. And I want to emphasize — there's no shame in using it."
    ate_jenny "A lot of students struggle silently. Homesickness, academic pressure, personal issues."
    ate_jenny "Our counselor is trained and compassionate. Walk-ins are accepted, but appointments are preferred."
    menu:
        "Where's the Student Handbook?":
            jump act6_jenny_handbook
        "(Good to know.)":
            jump act6_jenny_end

label act6_jenny_handbook:
    ate_jenny "The Student Handbook! Every student should have a copy."
    ate_jenny "It contains everything — the UP Student Code, academic policies, the student bill of rights, disciplinary procedures."
    ate_jenny "You can get a physical copy here at the OSA. We also have a digital version."
    ate_jenny "Key things to read:"
    ate_jenny "Section on Academic Regulations — absence policy, dropping procedures, leave of absence."
    ate_jenny "Section on Student Conduct — what's prohibited, what the penalties are."
    ate_jenny "Section on Student Rights — know your rights so you can stand up for them."
    ate_jenny "Section on Grievance Procedures — how to file a complaint if you're treated unfairly."
    player_char "I'll get a copy today."
    ate_jenny "Please do. When in doubt about any rule, the handbook is your source of truth."
    jump act6_jenny_end

label act6_jenny_end:
    ate_jenny "The OSA is here for you — always. Don't hesitate to drop by."
    ate_jenny "And enjoy Freshie Week! It only happens once."
    $ talked_ate_jenny = True
    $ complete_task("talk_ate_jenny")
    window hide
    return

## ============================================================================
## NPC 4 — COACH RAMON (Sports Coordinator)
## KEY INFO: Sports, physical education, inter-UP games
## ============================================================================
label act6_npc_coach_ramon:
    window show
    coach_ramon "You! Freshie! You look athletic. Do you play any sport?"
    player_char "I used to play a bit in high school..."
    coach_ramon "Perfect! I'm Coach Ramon. I handle the UPV varsity teams and PE classes."
    menu:
        "What sports are available at UPV?":
            jump act6_ramon_sports
        "How does PE work?":
            jump act6_ramon_pe
        "What are the inter-UP games?":
            jump act6_ramon_games

label act6_ramon_sports:
    coach_ramon "UPV has competitive teams in several sports:"
    coach_ramon "Basketball — men's and women's teams. Tryouts every start of semester."
    coach_ramon "Volleyball — very popular here. Strong program."
    coach_ramon "Swimming — makes sense, we're near the ocean."
    coach_ramon "Track and field — we train on the campus oval."
    coach_ramon "Sepak takraw — traditional sport, and UPV has some excellent players."
    coach_ramon "Martial arts — arnis and taekwondo clubs are active."
    coach_ramon "Football — growing program. We practice on the main field."
    player_char "Can freshmen try out for varsity?"
    coach_ramon "Absolutely! Tryouts are open to all enrolled students. Skill comes first, not seniority."
    coach_ramon "Varsity players also get some benefits — uniforms, travel allowance for competitions, and sometimes academic load adjustments."
    menu:
        "How does PE work?":
            jump act6_ramon_pe
        "What are the inter-UP games?":
            jump act6_ramon_games
        "(That's great info!)":
            jump act6_ramon_end

label act6_ramon_pe:
    coach_ramon "Physical Education — PE — is part of the GE curriculum. You'll take 4 PE units total."
    coach_ramon "PE 1 and PE 2 are usually assigned in your first year. PE 3 and PE 4 in second year."
    coach_ramon "Options include swimming, badminton, volleyball, dance, martial arts, and more."
    coach_ramon "Some PE classes are held at the gym. Others at the field or the pool."
    coach_ramon "PE grades are based on attendance, participation, and practical exams — not just fitness level."
    coach_ramon "Don't worry if you're not Athletic. The point is to stay active and learn basic movement skills."
    player_char "Is PE hard to pass?"
    coach_ramon "If you attend and participate, it's almost impossible to fail. Effort counts more than talent."
    menu:
        "What are the inter-UP games?":
            jump act6_ramon_games
        "(Thanks, Coach!)":
            jump act6_ramon_end

label act6_ramon_games:
    coach_ramon "The Inter-UP Games! The biggest sports event in the UP system."
    coach_ramon "All UP campuses send their best athletes to compete — Diliman, Los Baños, Visayas, Mindanao, and more."
    coach_ramon "It's held once a year, rotating between campuses. It's a week-long event."
    coach_ramon "Sports include basketball, volleyball, swimming, athletics, chess, table tennis, and more."
    coach_ramon "When UPV hosts, the entire campus transforms. Athletes from other campuses stay in our dorms."
    coach_ramon "It's the one time all UP students from across the country come together in friendly competition."
    player_char "That sounds amazing."
    coach_ramon "It IS amazing. And representing UPV? That's a badge of honor. Think about trying out."
    jump act6_ramon_end

label act6_ramon_end:
    coach_ramon "Remember — a healthy body supports a healthy mind. Don't neglect your physical well-being."
    coach_ramon "The gym is open 6 AM to 8 PM on weekdays. Free for students. No excuses!"
    $ talked_coach_ramon = True
    $ complete_task("talk_coach_ramon")
    window hide
    return

## ============================================================================
## ACT 6 COMPLETION — Org Fair Visit
## ============================================================================
label act6_org_fair:
    window show
    narrator_char "(You walk through the org fair. Banners of every color line the corridor.)"
    narrator_char "(Students call out to freshmen, handing out flyers, cracking jokes.)"
    narrator_char "(You sign up for two orgs. It feels like the start of something bigger than classes.)"
    narrator_char "\[ACT 6 COMPLETE] — Student Orgs & Campus Life."
    $ complete_task("visit_org_fair")
    window hide
    return

## ============================================================================
## END OF ACT 6 DIALOGUES
## ============================================================================
