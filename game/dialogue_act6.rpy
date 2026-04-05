## ============================================================================
## ACT 6 DIALOGUES — Student Orgs & Campus Life
## KEY THEME: Organizations, extracurriculars, campus events, scholarships
## ============================================================================

## --- ACT 6 INIT ---
label act6_start:
    # play music moved to end of previous act
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
    if "sq_org_culture" not in subquests_completed:
        menu:
            "★ Before I go — test me on org rules and the OSA.":
                jump sq_org_culture
            "(Thanks, Mika!)":
                pass
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
    kuya_tomas "The Scholarship Service office is right here — all scholarship processing, renewals, and certifications handled in one place."
    kuya_tomas "My door is always open. Actually — would you like to sit down properly and go through the process right now?"
    menu:
        "(Yes — walk me through the Scholarship Service properly.)":
            jump act6_visit_scholarship
        "(I'll come back another time, Kuya.)":
            jump act6_tomas_complete

label act6_tomas_complete:
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
    ate_jenny "Counseling services — through the GCSU. That's a big one."
    ate_jenny "Event permits — any org or student body event on campus needs OSA clearance."
    ate_jenny "Student welfare — dormitory concerns, emergency assistance, and student aid."
    player_char "What's the GCSU?"
    ate_jenny "The Guidance and Counseling Services Unit. It's one of the most important support services at UPV."
    menu:
        "Tell me more about the GCSU.":
            jump act6_jenny_gcsu
        "Where's the Student Handbook?":
            jump act6_jenny_handbook
        "(Good to know.)":
            jump act6_jenny_end

label act6_jenny_gcsu:
    ate_jenny "The GCSU provides professional counseling to all enrolled students — completely free and confidential."
    ate_jenny "They handle a lot of things:"
    ate_jenny "Individual counseling — for personal problems, family issues, anxiety, depression, or anything you're going through."
    ate_jenny "Academic counseling — if you're struggling with your grades, unsure about shifting programs, or feeling lost academically."
    ate_jenny "Career guidance — aptitude assessments, career planning, even mock interviews for graduating students."
    ate_jenny "Group counseling — they organize sessions on stress management, time management, and adjustment to college life."
    ate_jenny "Crisis intervention — if someone is in emotional distress or danger, the GCSU responds immediately."
    player_char "Is it really confidential? I'd feel embarrassed."
    ate_jenny "One hundred percent. Whatever you say stays between you and the counselor. That's professional ethics."
    ate_jenny "And there is NOTHING embarrassing about seeking help. The strongest students are the ones who ask for support."
    ate_jenny "Homesickness, burnout, relationship problems, family pressure — these are all valid reasons to visit."
    ate_jenny "Last semester, a student was about to drop out because of anxiety. The GCSU helped them through it. They graduated."
    ate_jenny "You can walk in during office hours or set an appointment. The GCSU office is at the Student Affairs area."
    player_char "I'll remember that. Thank you, Ate."
    ate_jenny "Please do. And if you notice a friend struggling — gently suggest they visit too."
    menu:
        "Where's the Student Handbook?":
            jump act6_jenny_handbook
        "(That's really important to know.)":
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
    if "sq_upv_events" not in subquests_completed:
        menu:
            "★ Quiz me on the UPV campus events calendar.":
                jump sq_upv_events
            "(Thanks, Ate Jenny!)":
                pass
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
## SUPPORT SERVICE VISIT — Scholarship Service
## Reference: UP Visayas Student Handbook — Financial Assistance & STFAP
## ============================================================================
label act6_visit_scholarship:
    window show
    narrator_char "(You sit across from Kuya Tomas at his desk. Bulletin boards behind him are covered in scholarship announcements, deadlines, and bracket tables.)"
    narrator_char "(A laminated sign reads: 'Scholarship Service — Office of Student Affairs. We process STFAP, University Scholarships, and all external financial assistance.'"
    kuya_tomas "Alright. Let me show you exactly what we do here and what you need to know."
    kuya_tomas "The Scholarship Service is the unit responsible for all student financial assistance at UPV."
    kuya_tomas "Think of us as the office that makes sure education doesn't stop because of money."
    menu:
        "Explain the STFAP — how does it work?":
            jump act6_schol_stfap
        "What documents do I need to apply?":
            jump act6_schol_documents
        "What are the STFAP brackets?":
            jump act6_schol_brackets
        "How do university and college scholarships work?":
            jump act6_schol_academic

label act6_schol_stfap:
    kuya_tomas "STFAP — Socialized Tuition and Financial Assistance Program — is UP's core equity mechanism."
    kuya_tomas "The University of the Philippines was built on the principle that no Filipino should be denied higher education because of poverty."
    kuya_tomas "STFAP implements that principle: your tuition is set based on your family's ability to pay."
    kuya_tomas "Every enrolled student is assigned a bracket — from A down to E9 — based on their household income and assets."
    kuya_tomas "Bracket A is the full standard assessment. Bracket E9 means zero tuition. The lower the bracket, the less you pay."
    player_char "Who decides my bracket?"
    kuya_tomas "You do, through your submitted documents. Our office evaluates them and conducts an interview if necessary."
    kuya_tomas "The key rule: SUBMIT HONESTLY. Misrepresentation — inflating poverty, hiding assets — is a disciplinary offense."
    kuya_tomas "If discovered, your scholarship is cancelled, you repay the difference, and you face academic sanctions."
    kuya_tomas "But if you're genuinely from a low-income family, DO NOT be ashamed to apply. That's exactly what STFAP is for."
    kuya_tomas "The application period opens at the start of each semester. Watch for announcements — the window is only two weeks."
    menu:
        "What documents do I need?":
            jump act6_schol_documents
        "What exactly are the brackets?":
            jump act6_schol_brackets
        "What about academic scholarships?":
            jump act6_schol_academic
        "(I understand the STFAP now.)":
            jump act6_schol_end

label act6_schol_documents:
    kuya_tomas "Here's the document checklist for STFAP application. I'll walk you through it."
    kuya_tomas "One — STFAP Application Form. Get it here or download from the UP website."
    kuya_tomas "Two — Income Tax Return (ITR) for the latest taxable year. Both parents, if employed."
    kuya_tomas "If your parents are self-employed or in informal work — a Sworn Affidavit of Income, notarized."
    kuya_tomas "If your family is below the tax threshold — a Certificate of Tax Exemption from the BIR."
    kuya_tomas "Three — Proof of assets: land title or tax declaration for property, OR an affidavit that you own none."
    kuya_tomas "Vehicle registration if your family owns a vehicle. Bank certificates for savings accounts."
    kuya_tomas "Four — Certificate of Employment or business permit for parents, if applicable."
    kuya_tomas "Five — PSA Birth Certificate and your parents' PSA Marriage Certificate."
    kuya_tomas "Six — latest electric bill or water bill — shows actual household usage and provides address verification."
    player_char "What if I can't get some of these documents in time?"
    kuya_tomas "Come to us and explain your situation. We can advise you on alternatives."
    kuya_tomas "For instance, if your father is an OFW, we accept a contract copy and remittance records in place of an ITR."
    kuya_tomas "Single-parent households have a different document set. Come see us — we handle cases individually."
    kuya_tomas "The most important thing: DO NOT miss the deadline trying to get the perfect set of documents."
    kuya_tomas "Submit what you have and note what's missing. We'll work with you."
    menu:
        "What are the STFAP brackets?":
            jump act6_schol_brackets
        "Tell me about academic scholarships.":
            jump act6_schol_academic
        "(I'll start gathering documents.)":
            jump act6_schol_end

label act6_schol_brackets:
    kuya_tomas "Let me show you the bracket table."
    narrator_char "(He slides a laminated chart across the desk. You study it carefully.)"
    kuya_tomas "Bracket A — full tuition at the standard assessed rate. This is the DEFAULT if you don't file STFAP."
    kuya_tomas "Never skip filing just because you think you're Bracket A. You might qualify for something lower."
    kuya_tomas "Brackets B and C — reduced tuition. Partial exemptions based on income thresholds."
    kuya_tomas "Bracket D — significantly reduced. Tuition drops to around ₱300 per unit or lower."
    kuya_tomas "Brackets E1 through E4 — very low to near-zero tuition. These cover families earning below the poverty line."
    kuya_tomas "Brackets E5 through E9 — ZERO tuition. Families with very limited income pay nothing."
    player_char "Are there any cash benefits for the lower brackets?"
    kuya_tomas "Yes. Brackets E5 to E9 may also include a monthly living allowance — around ₱1,000 to ₱4,000 depending on the sub-bracket."
    kuya_tomas "This is separate from any external scholarship stipend you may receive."
    kuya_tomas "You CAN receive STFAP benefits and a DOST or private scholarship simultaneously — they don't cancel each other out."
    kuya_tomas "Important: your bracket must be renewed every academic year. If your family's situation changes significantly, you must update it."
    menu:
        "How do academic scholarships work?":
            jump act6_schol_academic
        "What documents do I need?":
            jump act6_schol_documents
        "(That's very clear.)":
            jump act6_schol_end

label act6_schol_academic:
    kuya_tomas "Academic scholarships at UP are automatic — no application needed. They're based entirely on your GWA."
    kuya_tomas "University Scholar — GWA of 1.20 or better at the end of the semester, with NO grade of 5.00 or INC."
    kuya_tomas "University Scholars are exempted from ALL tuition and miscellaneous fees. Full exemption."
    kuya_tomas "College Scholar — GWA of 1.45 or better. Same conditions apply — no 5.00 or INC."
    kuya_tomas "College Scholars receive a partial to full exemption depending on their college's rules."
    kuya_tomas "Dean's Lister — GWA of 1.75 or better. Academic recognition; no tuition benefit but it carries prestige."
    player_char "Can I be both a University Scholar AND receive STFAP benefits?"
    kuya_tomas "Yes! These are independent systems. University Scholar removes tuition fees through academic merit."
    kuya_tomas "STFAP sets your tuition based on income. If you're a University Scholar, your tuition is already zero — so STFAP still applies to miscellaneous fees."
    kuya_tomas "And you can stack external scholarships on top of all of these. UP doesn't limit scholarship stacking."
    kuya_tomas "The catch: most scholarships require you to MAINTAIN a minimum GWA — usually 2.00 or better."
    kuya_tomas "Fall below, and you get one semester of probation. Don't recover — scholarship is suspended or revoked."
    player_char "What does the Scholarship Service do beyond STFAP and academic scholarships?"
    kuya_tomas "We process and verify ALL types — government grants like DOST and CHED, private foundation awards, LGU assistance."
    kuya_tomas "We issue official certifications: enrollment verification, good moral character, certified true copies of grades."
    kuya_tomas "These are what scholarship sponsors need to release your stipend or renew your grant."
    kuya_tomas "We also post new scholarship announcements on our bulletin board first — before social media. Check it every week."
    jump act6_schol_end

label act6_schol_end:
    narrator_char "(Kuya Tomas hands you a folder: STFAP Application Form, Document Checklist, and the Bracket Table.)"
    kuya_tomas "This is your starter pack. Read everything. Come back with questions."
    kuya_tomas "Remember — financial hardship is not a barrier at UP. It is something we are designed to address."
    kuya_tomas "Use the system. It exists for you."
    narrator_char "(Encyclopedia unlocked: Scholarship Service.)"
    $ persistent.encyclopedia_unlocks.add("scholarship_service")
    $ talked_kuya_tomas = True
    $ complete_task("talk_kuya_tomas")
    $ complete_task("visit_scholarship_service")
    window hide
    return

## ============================================================================
## NPC 5 — DAN (Returning from Act 5 — Financial Stress / GCSU Referral)
## KEY INFO: Financial hardship, GCSU preventive counseling, New Admin scholarship
## ============================================================================
label act6_npc_dan:
    window show
    narrator_char "(You spot Dan from your Kas 1 class sitting alone on a bench near the CAS corridor. He's staring at his phone — not really looking at anything.)"
    player_char "Dan? Hey."
    dan "Oh — hey."
    player_char "You look rough. What's going on?"
    dan "I'm fine. It's nothing."
    player_char "You're sitting alone staring at your phone during Freshie Week. That's not nothing."
    dan "..."
    dan "My allowance didn't come in. My parents are dealing with something back home and they couldn't send anything this month."
    dan "I've got fifty pesos left. I don't know how I'm going to eat, buy printing supplies, pay for the commute back to the dorm..."
    player_char "Have you talked to anyone about it? The guidance office, maybe?"
    dan "The guidance office? That's for people who are — I don't know. Mentally falling apart or something."
    player_char "It's not only for that. Ate Jenny was just telling me the GCSU handles academic stress, financial problems, all of it."
    player_char "They also connect students to emergency financial assistance."
    dan "Emergency financial assistance? That's a thing here?"
    player_char "Apparently. Come on — let's go find out."
    dan "...You'd come with me?"
    player_char "You walked me to the HSU in Act 5. I owe you one."
    jump act6_visit_gcsu_dan

label act6_visit_gcsu_dan:
    narrator_char "(The Guidance and Counseling Services Unit. A quiet room near the Office of Student Affairs. A small sign on the door: 'GCSU — All sessions are confidential. Walk-ins welcome.')"
    narrator_char "(Inside: calm lighting, a few chairs, some plants on the windowsill. A counselor looks up from her desk with a steady, welcoming expression.)"
    guidance_counselor "Good afternoon. Come in — both of you. I'm Ma'am Garcia."
    guidance_counselor "Please, sit. Take a breath. There's no rush here."
    dan "Hi, Ma'am. I'm — I'm not sure if this is the right place, but my classmate said—"
    guidance_counselor "This is exactly the right place. Whatever brought you here is valid."
    guidance_counselor "Take your time."
    dan "I'm a first-semester freshman. My allowance from home didn't come in this month. My family is going through something."
    dan "I have fifty pesos left. I don't know how to get through the next few weeks. And I didn't know who to tell."
    guidance_counselor "Thank you for saying that out loud. I know it takes courage."
    guidance_counselor "What you're feeling right now — the stress, the uncertainty, the shame of asking for help — those are real. And you are not alone in feeling them."
    guidance_counselor "Financial pressure is one of the most common reasons freshmen struggle in their first semester. Most suffer in silence. You didn't. That matters."
    dan "I kept thinking I should be able to handle it myself."
    guidance_counselor "That belief — that you have to manage everything alone — is one we want to gently work through today."
    guidance_counselor "Asking for help is not weakness. It is one of the wisest things a person can do."
    guidance_counselor "Let's start simply. Can you take a slow breath with me?"
    guidance_counselor "In... hold... and out."
    narrator_char "(A quiet moment passes. You watch Dan breathe. Something in his posture settles — just slightly.)"
    guidance_counselor "Good. Let me tell you what the GCSU can offer."
    guidance_counselor "We provide preventive counseling — sessions like this one, designed to help students before a difficulty becomes a crisis."
    guidance_counselor "We also do individual follow-up sessions, group support, stress management workshops, and crisis intervention when things become serious."
    guidance_counselor "Today I want to do two things with you."
    guidance_counselor "First — remind you that this situation is temporary, and it says nothing about your capability."
    guidance_counselor "Second — connect you with the office that can help you get through this month."
    dan "There's an office for that?"
    guidance_counselor "Yes. The Scholarship Service at the New Administration Building."
    guidance_counselor "They handle emergency financial assistance — a Student Emergency Fund that can cover meals, photocopying, and basic transport while you stabilize."
    guidance_counselor "They also process STFAP re-bracketing. If your family's financial situation changed, you can request a reassessment — which may lower your tuition next semester."
    guidance_counselor "And they can show you scholarship programs with monthly stipends you may still qualify to apply for."
    player_char "So there's actually quite a lot available."
    guidance_counselor "More than most students know about. That's exactly why this referral system exists."
    guidance_counselor "I'm writing you a referral letter to the Scholarship Service now. It helps them prioritize urgent cases."
    guidance_counselor "Bring it to the New Admin Building. Ask for Kuya Tomas. Tell him I sent you."
    dan "I... thank you, Ma'am. I really didn't think anyone here would care about something like this."
    guidance_counselor "We care. That is what this office is for."
    guidance_counselor "Come back and see me, even after this is resolved, Dan. Adjusting to college life is hard — with or without financial pressure."
    guidance_counselor "My door is always open."
    narrator_char "(Ma'am Garcia seals a referral envelope and hands it to Dan along with a small pamphlet: 'GCSU — Because You Matter.')"
    narrator_char "(Dan holds it carefully. Like it means something. Because it does.)"
    jump act6_dan_new_admin

label act6_dan_new_admin:
    narrator_char "(You walk with Dan to the New Administration Building. Kuya Tomas is at his desk. He reads the referral letter, sets it down, and opens a folder.)"
    kuya_tomas "Referral from Ma'am Garcia. Sit down."
    kuya_tomas "Okay — let's talk about what we can do."
    kuya_tomas "First — the Student Emergency Assistance Fund. This covers immediate needs: meals, photocopying, basic transport. Up to ₱1,500, processed in 24 to 48 hours."
    kuya_tomas "I'll flag your case as urgent. You should have something by end of week."
    dan "That would really help."
    kuya_tomas "Second — STFAP re-bracketing. If your family's financial situation changed this semester, we reassess your bracket."
    kuya_tomas "A lower bracket means lower tuition. Some brackets include a monthly living allowance — ₱1,000 to ₱4,000 depending on your assessment."
    kuya_tomas "Third — here's a list of scholarship programs with applications open this month."
    narrator_char "(He slides a printed sheet across the desk. Dan scans it. His eyes stop at the stipend amounts.)"
    dan "Some of these give ₱3,000 a month?"
    kuya_tomas "Some give more. The key is applying on time. Deadlines are strict — one day late means disqualification."
    kuya_tomas "Fill out this form. Student number, contact details, and a brief description of your situation. We'll start the emergency fund process today."
    player_char "Is there anything else he should know?"
    kuya_tomas "Keep a folder — grades, income certificate, all your documents. When scholarship season opens, you grab it and go. No scrambling."
    kuya_tomas "And check this bulletin board every week. New scholarship announcements go up every Monday."
    kuya_tomas "You're not the first student in this chair. You won't be the last."
    kuya_tomas "UP has been doing this for over a hundred years. We don't let students fall through the cracks."
    narrator_char "(Dan fills out the form. His hands are steady.)"
    narrator_char "(An hour ago he was on a bench with fifty pesos and no path forward.)"
    narrator_char "(Now he has an emergency fund in motion, a scholarship list, and a follow-up session at the GCSU.)"
    player_char "(This is what a support system looks like when it actually works.)"
    narrator_char "(Encyclopedia unlocked: GCSU — Guidance and Counseling Services Unit.)"
    $ persistent.encyclopedia_unlocks.add("gcsu")
    $ complete_task("talk_dan_gcsu")
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
play music "audio/Act7.mp3" fadein 1.0
