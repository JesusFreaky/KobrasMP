# KOBRASMP AI PROJECT STATE

> CANONICAL MACHINE-ORIENTED CONTINUITY LEDGER
> Purpose: reconstruct project intent, verified technical knowledge, failed approaches, invariants, workflow, and current state across ChatGPT conversations/context resets.
> Audience priority: future AI agents working on KobrasMP. Human readability is secondary.
> Update rule: after any material architectural/balance/runtime discovery, update this file on `experimental`. Never silently overwrite a VERIFIED fact with an inference.

STATE_SCHEMA
- HARD_RULE = binding project invariant unless user explicitly changes it.
- VERIFIED_REPO = physically confirmed in current repository/commit/diff.
- VERIFIED_VANILLA = physically confirmed against EU4 Vanilla 1.37 source.
- VERIFIED_RUNTIME = user/in-game test confirmed.
- APPROVED_DESIGN = user-approved intent; not proof of implementation/runtime behavior.
- UNVERIFIED = plausible/current implementation but requires runtime or deeper engine certification.
- FAILED = attempted approach explicitly rejected/broken; retain lesson to prevent recurrence.
- SUPERSEDED = historically relevant but no longer current design.
- PENDING = known work/test not completed.

===============================================================================
PROJECT_IDENTITY
===============================================================================
PROJECT = KobrasMP
GAME = Europa Universalis IV
TARGET_SUPPORTED_VERSION = 1.37.*
REPOSITORY = JesusFreaky/KobrasMP
STABLE_BRANCH = main
DEVELOPMENT_BRANCH = experimental
CURRENT_LEDGER_CREATED_FROM_EXPERIMENTAL_HEAD = 19d21983cd08c03309322babb35123ffeb3b7b92
CURRENT_HEAD_MESSAGE_AT_LEDGER_CREATION = balance: enforce deterministic early-game AI outcomes

[HARD_RULE] Branch semantics
- `main` = stable/release baseline; 1.6 is RELEASE / PRE-MISSIONS FINAL baseline.
- `experimental` = future development / 1.7 work.
- Normal work targets `experimental`.
- Do not merge/promote to `main` unless user explicitly approves tested result.

[HARD_RULE] Physical state beats conversational checkpoints
- BEFORE ANY REPOSITORY ALTERATION: physically fetch/verify current `experimental` HEAD.
- Never assume an SHA copied from an old HTML/chat/checkpoint remains HEAD.
- Never claim commit/push/update unless GitHub operation confirms it.
- Compare final commit against intended parent and audit changed files.

===============================================================================
SOURCE AUTHORITY / EVIDENCE ORDER
===============================================================================
[HARD_RULE]
1. EU4 Vanilla 1.37 files = primary syntax/scope/effect/trigger architecture authority.
2. Zlewikk-MJL Multiplayer Rebalance Pack = primary MP/performance/architecture benchmark.
3. Gekko v9 = secondary balance/aggression reference.
4. Expanded Universalis = creative mission/mechanics reference, NOT syntax authority over Vanilla.
5. Existing Kobras implementation = behavioral contract when already approved/tested, unless user requests redesign.

Local/reference artifacts historically available to project sessions include:
- Arquivos Vanilla(1).zip
- Zlewikk-MJL Multiplayer Rebalance Pack(1).zip
- Gekko V9 (bastard x gecko)(1).zip
- Expanded Universalis(1).zip
- Kobras 1.6 - Pre Missions Final.zip
- archived EU4 Modding HTML conversations/checkpoints.
These artifacts may not exist in every future runtime. Prefer repository + current uploaded Vanilla/reference files when available.

===============================================================================
GLOBAL ENGINE / MODDING HARD RULES
===============================================================================
[HARD_RULE] Never invent Clausewitz/EU4 syntax.
- Do not import syntax/scopes/effects from CK/Stellaris/HOI/Victoria or generic Paradox intuition.
- Validate unfamiliar trigger/effect/scope against actual Vanilla 1.37 or legitimate reference implementation.
- If not physically verified, label UNVERIFIED rather than presenting as fact.

[HARD_RULE] MP determinism/performance
- KobrasMP is multiplayer-first.
- Avoid unnecessarily expensive global scans, repeated broad `any_*` scopes, event polling, or complex triggers when simpler deterministic architecture exists.
- Prefer Vanilla-established event architecture and Zlewikk-style simplification.
- Prefer triggered modifiers where they safely replace repeated polling.
- Do not trade determinism/OOS safety for decorative complexity.

[HARD_RULE] Scope discipline
- Read event scope before editing. ROOT/FROM/THIS/owner semantics must be proven from surrounding Vanilla architecture.
- `create_union` semantics VERIFIED: scoped country becomes senior over target. Example relevant to current implementation: `HAB = { create_union = HUN }` => Austria senior, Hungary junior.
- Previous PAP/Cawa investigation VERIFIED: `on_cawa_raised` documents THIS as Province; country effects must resolve through `owner`, not guessed `FROM`.
- Previous mission work VERIFIED: use `not_in_mission_preview_mode` following Vanilla mission preview architecture.

[HARD_RULE] Atomicity
- Prefer one coherent atomic commit per requested logical change set.
- Do not generate incidental workflow/helper/debug files in final tree.
- Temporary technical branches/workflows are acceptable only if removed/excluded from final target tree and final target commit contains exactly intended content.

===============================================================================
RELEASE / 1.6 BASELINE
===============================================================================
[VERIFIED_REPO/HISTORICAL]
1.6 = RELEASE / PRE-MISSIONS FINAL foundation.
Mission reset to Vanilla for:
- Bavaria
- Burgundy
- Milan
- Papal State
- Jerusalem/Crusader
- Cologne/Lotharingia
Exceptions retained at 1.6 checkpoint:
- Angevin custom/adjusted.
- Serbia custom state retained.

Known release-era fixes/state:
- Milan starts with 40 legitimacy via `add_legitimacy = -60` to support republican event behavior.
- Rügen and Modena history/government setup BOM issues fixed; monarchy + feudalism_reform preserved.
- HRE minors disappearance in intermediate build was repaired/restored.
- Aragon high autonomy issue corrected.
- Teutonic ruler/government/heredity work adjusted; user later specifically wanted Teutonic ruler 3/3/5.

[HARD_RULE] Do not casually regress 1.6 fixes while importing Vanilla files. If replacing a whole Vanilla-derived file, diff against Kobras first because Kobras may contain unrelated fixes.

===============================================================================
MISSION TREE GLOBAL DESIGN CONTRACT FOR 1.7
===============================================================================
[HARD_RULE]
- Use all five horizontal mission slots where a custom tree is genuinely being built.
- Avoid narrow left-stacked trees.
- Branches may converge/diverge when meaningful.
- No generic bastion/economy/HRE missions mixed into nations with intended custom trees.
- A mission must produce meaningful gameplay change. Mana/prestige may be secondary garnish, not the primary content of large portions of a tree.
- Do NOT solve mana/prestige filler by replacing it with generic country_modifier spam.
- Rewards should preferentially use contextual systems: events, CBs, PU/subjects, conversion/regional effects, government/reforms, estates, Great Projects, diplomacy, claims/cores when justified, economic development, fortifications, military support, world interaction.
- Mission count is emergent from meaningful content. No arbitrary target such as 75.
- Expanded Universalis may inspire mechanics, but does not justify tree inflation.

[HARD_RULE] Mission workflow
nation -> inspect Vanilla + references -> understand existing mechanics -> present conceptual changes -> user approves design/balance -> implement -> static syntax/scope validation -> runtime test -> consolidate.
Do not treat conceptual approval as runtime certification.

===============================================================================
PAPAL STATE: CRITICAL FAILED APPROACH + CURRENT POLICY
===============================================================================
[FAILED][DO_NOT_REPEAT]
Name = PAP Mission Tree v2.2 full custom rework
Historical architecture:
- ~75 custom missions.
- Four exclusive paths: Austria / France / Spain / Autonomous.
- Branch selection around `The Temporal Sword`.
- Guard of Saint Peter/Cawa staged system.
- Large custom localisation/pathing/preview architecture.
Failure mode observed by user in runtime/UI review:
- tree structurally large but mechanically hollow;
- excessive prestige/mana rewards;
- supposed world-interaction missions often did not actually interact meaningfully with external countries;
- mission count became a target rather than a consequence of gameplay needs;
- implementation contradicted explicit 1.7 philosophy.
Lesson:
- structural completeness != mechanical completeness;
- never mark a tree complete because triggers/pathing/localisation compile;
- every mission must answer: `what concrete change does this produce in the game/world?`
- `55 excellent missions > 75 filler missions` is representative design principle, not a required count.

[VERIFIED_REPO]
Full PAP rework rollback commit:
- `2b7f73cb82c20d60ea5e7e63cf55ae9a2fbb1355`
- message: `revert: remove Papal rework and restore pre-PAP baseline`
Rollback target content matched pre-PAP baseline tree exactly; comparison against pre-PAP baseline produced no residual file differences.
Therefore residual content from PAP v2.2 in active experimental tree at rollback = ZERO.
Important nuance: pre-existing Papal/Vanilla content that existed before v2.2 naturally remains; only v2.2 cycle was removed.

[APPROVED_DESIGN][CURRENT_PAP_POLICY]
- Do NOT rebuild a large custom Papal mission tree from scratch.
- Vanilla Papal mission preset/tree is mandatory physical/structural base for future PAP work.
- Modify existing Vanilla rewards and, when useful, triggers/localisation so it no longer feels like unchanged Vanilla.
- Add a new mission only when a strong mechanic cannot reasonably fit an existing Vanilla node.
- Candidate selective custom systems/ideas: Guard of Saint Peter, Naples interaction, Papal Intervention, Holy League. These are ideas, NOT currently implemented merely because they existed in failed v2.2.
- Reuse Vanilla positions/connections/pathing whenever possible.
- Review incrementally mission-by-mission.
- Old v2.2 can be used only as idea bank; never as primary base.

[SUPERSEDED][PAP_IDEA_BANK_NOT_ACTIVE]
Old PAP identity that may remain conceptually useful if user revives pieces:
- Territorial expansion focused Italy + North Africa.
- Influence/intervention across Catholic world.
- Military identity: morale, manpower, reinforce, resistance, fortifications; avoid Discipline/ICA powerhouse.
- Economy: Tax + Development; Genoa as Papal economic axis; do not require Venezia/Venice node.
- Concept phrase: `The Pope does not conquer Europe; he moves the pieces of Europe.`
- External support should strengthen Catholic countries/regions rather than merely reward PAP with mana/prestige.
Do not assume these are current implemented mechanics.

[SUPERSEDED][TECHNICAL_LESSONS_FROM_REVERTED_GUARD]
These are retained as engine lessons only, not active feature state:
- Cawa Vanilla base keys observed: `shock_damage_received`, `land_attrition`, `reinforce_speed`, `amount_of_cawa`, `morale_damage`, `morale_damage_received`, `is_cawa_modifier`, `allow_cawa`.
- Papal Guard staged triggered-modifier behavior with `is_cawa_modifier + amount_of_cawa` was never fully runtime-certified.
- Origins DLC conditionality mattered for `allow_cawa`.
- Do not resurrect these files blindly.

===============================================================================
BURGUNDY / MARIE / SUCCESSION
===============================================================================
[VERIFIED_REPO/HISTORICAL]
Kobras contains custom Burgundian Succession/Marie work predating PAP rollback and it was intentionally preserved by PAP rollback.
Known design history:
- user preferred simplified succession without unnecessary dispute complexity.
- earlier issue: mission `resolve the burgundian succession` not enabling / imperial incident behavior required verification.
- Austria-related Burgundian succession changes existed immediately before PAP work and were explicitly preserved when PAP was reverted.

[HARD_RULE]
Before modifying Burgundian succession, inspect current repo implementation. Do not reconstruct from old chat memory because this chain has been iterated repeatedly.

===============================================================================
CURRENT DETERMINISTIC EARLY-GAME AI PACKAGE
===============================================================================
[VERIFIED_REPO]
Commit = `19d21983cd08c03309322babb35123ffeb3b7b92`
Message = `balance: enforce deterministic early-game AI outcomes`
Parent = PAP rollback commit `2b7f73cb82c20d60ea5e7e63cf55ae9a2fbb1355`
Exactly four target files changed:
- `Kobras/history/countries/HAB - Austria.txt`
- `Kobras/events/flavorHUN.txt`
- `Kobras/events/flavorMOL.txt`
- `Kobras/events/FlavorFRA.txt`
Static assembly used exact Vanilla-derived blocks and `git diff --check`; final commit was audited as one commit over intended parent.

[VERIFIED_REPO] Austria / Ladislaus Postumus
File = `Kobras/history/countries/HAB - Austria.txt`
- 1440.2.22 heir Ladislaus Postumus stats changed 3/3/3 -> 4/4/4.
- 1452.1.1 historical monarch Ladislaus Postumus stats also changed 3/3/3 -> 4/4/4 for consistency.
- Dynasty/birth/death/name preserved.
Intent = Austria begins with Ladislaus as 4/4/4 and historical ruler transition does not downgrade him.

[VERIFIED_REPO][VERIFIED_VANILLA_SCOPE] Hungary -> Austrian PU deterministic AI path
File = `Kobras/events/flavorHUN.txt`
Main event = `flavor_hun.2`
Current AI weighting:
- Mátyás option = `factor = 0`.
- Austrian union option `flavor_hun.2.b` = `factor = 100`.
- alternative third option = `factor = 0`.
Union effect remains Vanilla architecture:
`HAB = { create_union = HUN }`
Semantics confirmed: Austria/HAB = senior partner; Hungary/HUN = junior partner.
Before union, if Hungary is senior over Croatia, event inherits CRO into HUN; then HAB creates union over HUN. This avoids nested Hungarian PU over Croatia.

Critical bypass discovered during implementation:
- Vanilla event `flavor_hun.201` (`Ladislaus Postumus dies of Leukemia`) can independently derail deterministic Austrian PU by killing Ladislaus/allowing alternate succession.
- Current Kobras adds `ai = no` to the REAL trigger of `flavor_hun.201`.
- This blocks this bypass for AI Hungary while preserving Vanilla event availability for a human player.
- Earlier implementation attempt accidentally considered placing this restriction in a description sub-trigger; caught before final commit and corrected to actual event trigger. DO NOT regress this distinction.

[UNVERIFIED_RUNTIME]
The Hungarian deterministic chain is statically/scope verified but should still be tested in an actual campaign through relevant 1450s succession timing. If runtime result differs, inspect all alternate HUN succession events before changing `create_union` semantics; the union direction itself is verified correct.

[VERIFIED_REPO] Moldavia -> Poland deterministic AI choice
File = `Kobras/events/flavorMOL.txt`
Event = `flavor_mol.2`
- Polish March = `factor = 100`.
- Hungarian March = `factor = 0`.
- Independence = `factor = 0`.
- Vanilla modifier that multiplied Hungarian choice under `has_global_flag = hun_moldavia_hungarian_alliance` removed because base Hungarian factor is intentionally zero.
Important implementation lesson: flag is GLOBAL (`has_global_flag`), not country flag. A preliminary automated assertion assumed country flag and correctly aborted before content commit. Do not repeat that mistaken flag type.

[UNVERIFIED_RUNTIME]
Static event weighting deterministic if options are available. If Polish option becomes unavailable due to external game-state triggers elsewhere, inspect event trigger/option availability before claiming impossible state. Current requested behavior is AI weighting, not forced script bypass of all game-state legality.

[VERIFIED_REPO] England / Surrender of Maine / Hundred Years War
File = `Kobras/events/FlavorFRA.txt`
English Maine event = `flavor_fra.6`
- England cedes Maine option `flavor_fra.6.a` = `factor = 0`.
- England refuses option `flavor_fra.6.b` = `factor = 100`.
- Vanilla modifiers that could zero refusal while at war or in a disaster were removed, because they contradicted deterministic refusal goal.
French response = `flavor_fra.7`
- war response = `factor = 100`.
- preserve-peace response = `factor = 0`.
- war effect remains Vanilla `ENG = { declare_war_with_cb = { who = FRA casus_belli = cb_hundred_years_war } }`.
Reason for modifying BOTH English and French choices: forcing England to refuse Maine alone does not guarantee the chain becomes war if France can select its peace branch.

[UNVERIFIED_RUNTIME]
This guarantees deterministic AI choices when the Surrender of Maine event chain fires and options are legal. It does NOT rewrite the upstream event trigger/MTTH to force the event to fire under game states where Vanilla trigger conditions fail. User wording `always declares HYW` was implemented as deterministic choice chain, not unconditional day-1 scripted war.

===============================================================================
KNOWN RULER / HISTORY INTENT FROM PRIOR PROJECT WORK
===============================================================================
[HISTORICAL_CONTEXT; VERIFY_REPO_BEFORE_EDITING]
Previously requested/implemented ruler intentions include:
- Serbia king age 25.
- Byzantine ruler 4/4/4.
- Georgia Bagrationi ruler 4/4/4 + heir age 5 4/4/4.
- Teutonic ruler ultimately requested 3/3/5 (earlier intermediate 3/3/6 existed).
- Scotland ruler 4/4/5.
- Jerusalem heir age 5 4/4/4.
- Karabakh ruler age 25 4/4/4 + heir age 5 4/4/4 with historical dynasty.
- Milan legitimacy 40.
- No-ruler issues historically included Corsica, Tabriz, Bulgaria, Pisa, Osnabrück, Calenberg, Coburg, Lusatia, later Modena/Rügen.
These are NOT all re-audited at ledger creation. Treat as historical intent and inspect current physical files before touching.

[HARD_RULE] History audit
- Audit dates before 1444 when changing country/province histories; old monarch/occupation entries can unexpectedly override 1444 setup.
- Avoid false positives from only reading visible 1444 block.
- User historically requested bringing untouched Vanilla history into Kobras for future editing; therefore presence of a Vanilla-like history file does not itself imply it was custom-modified.

===============================================================================
MERCENARY POLICY
===============================================================================
[APPROVED_DESIGN/HISTORICAL]
- Keep Kobras custom companies + Vanilla companies specifically unlocked by national content (mission/decision/reform/event).
- Remove generic Independent Company, Free Company, Grand Company and other generic clutter.
- Examples of legitimate national-content companies: Black Army, Swiss Guard, Danish/national companies where unlocked by content.
- Custom Siege Companies 10/15/20/25 existed historically.
- Tiny Company requested: 6 infantry, no cavalry.
- Large company correction requested: 4 cavalry rather than 3.
- Cavalry/artillery company cost reductions of 5% requested historically.
- Manpower pool implementation was flagged for verification against Vanilla/Zlewikk.

[HARD_RULE]
Do not assume historical mercenary numbers are current without fetching files. This section preserves design intent, not full current certification.

===============================================================================
KNOWN GOOD / KNOWN PROBLEM HISTORY
===============================================================================
[VERIFIED_RUNTIME/HISTORICAL USER REPORTS]
Reported working in earlier 1.6 testing:
- Nordic decision.
- Cossack decision.
- Poland/Marie behavior reported OK at one checkpoint.
- new custom mercenaries appeared, though generic Vanilla companies still appeared and required policy cleanup.
- Teutonic adjustments eventually tested/iterated.

[HISTORICAL PROBLEMS; SOME SUPERSEDED BY RESET]
- Bavaria/Milan/Papal/KOJ mission pathing bugs existed before mission reset; reset to Vanilla removed those custom mission implementations.
- Jerusalem modifier localisation/pathing issues existed before reset.
- generic missions appearing alongside custom trees was explicitly unwanted.
- Burgundian resolve-succession mission/imperial incident required verification.
- HRE minors disappeared in intermediate build then were restored.

===============================================================================
FAILED / ABORTED IMPLEMENTATION LESSONS
===============================================================================
[FAILED][DO_NOT_REPEAT]
1. PAP v2.2 large custom tree: see dedicated PAP section.
2. Never use arbitrary mission count as quality target.
3. Never interpret `mana/prestige reward exists` as mission mechanically complete.
4. Never replace filler with generic modifier filler.
5. Never assume a preview branch is functional because localisation/pathing looks correct; branch selection and preview require real architecture + runtime test.
6. Never assume event option factor change alone guarantees outcome if a downstream country gets another choice; Maine chain required both ENG and FRA weighting.
7. Never make Hungarian PU deterministic only by changing `flavor_hun.2`; alternate `flavor_hun.201` was a bypass and needed AI handling.
8. Never put an event-level restriction inside a description trigger. Description `desc = { trigger = {...} }` only controls description selection. Real event `trigger = {...}` controls firing.
9. Moldavia Hungarian alliance flag is global, not country flag.
10. `HAB = { create_union = HUN }` is NOT reversed; HAB is senior. Do not “fix” it into HUN scope based on intuition.
11. Previous Cawa on_action lesson: do not use guessed FROM when Vanilla documents THIS=Province; resolve owner.
12. Do not import Milan modifiers or unrelated national modifiers into another tag simply because keys compile.
13. Do not use invalid/non-Vanilla scopes such as previously attempted `any_allied_country`; use verified Vanilla scopes.
14. Do not write/commit from stale SHA/checkpoint.
15. Do not leave temporary workflow/build machinery in experimental final tree.

===============================================================================
PAP / NAPLES EVENT RESEARCH RETAINED AS KNOWLEDGE ONLY
===============================================================================
[VERIFIED_VANILLA][NOT_CURRENTLY_IMPLEMENTED_AS_CUSTOM_PAP]
Vanilla Neapolitan succession chain relevant if future PAP work revisits Naples:
- `flavor_ara.7` Neapolitan Succession requires ARA no longer has ruler Alfons V, flag conditions, NAP junior union with ARA, before 1500; MTTH ~2 months once eligible. Therefore it does NOT fire merely because one year passed.
- follow-up `flavor_ara.8` can break union and involve PAP.
- PAP `flavor_ara.9` can provide paths including a long vassalization CB against NAP (`cb_vassalize_mission`, 600 months in inspected Vanilla implementation).
- Vanilla does not simply hand Naples to Pope.
Use this chain as reference if user requests a targeted Naples mechanic; do not recreate old PAP mission blindly.

===============================================================================
WORKFLOW FOR FUTURE AI AGENT
===============================================================================
[HARD_RULE][BOOT_SEQUENCE]
When a new conversation asks to continue KobrasMP:
1. Read this entire ledger first.
2. Fetch current `experimental` branch HEAD; compare to ledger recorded HEAD if relevant.
3. If HEAD advanced, inspect commits/diff since ledger update and reconcile ledger before major work.
4. Fetch exact files relevant to requested change.
5. If syntax/mechanics unfamiliar, inspect Vanilla 1.37 implementation before proposing code.
6. Separate DESIGN intent from IMPLEMENTATION fact from RUNTIME evidence.
7. Make smallest coherent change that satisfies user.
8. Static audit: syntax patterns/scopes, accidental file changes, diff size, localisation references where relevant.
9. Commit atomically.
10. Verify final branch HEAD and diff.
11. Update this ledger when the change teaches a durable rule, adds a major system, resolves a pending uncertainty, or records a failed approach worth remembering.

[HARD_RULE][USER_COMMUNICATION]
- Portuguese by default.
- Concise/technical/copyable.
- User wants context-budget estimate in every KobrasMP/EU4 project response: report approximate `% used / % remaining`.
- If likely to hit context limit during requested work, STOP before starting and provide a complete self-contained checkpoint for next chat.
- Do not spam ZIPs/files each pass; only consolidate/export when requested.

===============================================================================
REPOSITORY SAFETY CHECKLIST
===============================================================================
Before write:
- [ ] current experimental HEAD physically fetched
- [ ] target file fetched from current HEAD
- [ ] unrelated Kobras customizations identified/preserved
- [ ] Vanilla syntax/source checked where needed
- [ ] user-approved design not silently expanded

Before commit:
- [ ] only intended files changed
- [ ] no temp workflow/debug/helper files
- [ ] no stale localisation IDs introduced
- [ ] no invalid scope/effect guessed
- [ ] deterministic/MP implications considered
- [ ] event chains checked downstream, not only first choice

After commit:
- [ ] commit SHA confirmed
- [ ] branch ref confirmed
- [ ] compare parent..commit inspected
- [ ] runtime-dependent claims labelled UNVERIFIED until tested
- [ ] ledger updated if durable knowledge changed

===============================================================================
CURRENT IMMEDIATE STATE AT LEDGER CREATION
===============================================================================
[VERIFIED_REPO]
`experimental` HEAD before adding this ledger = `19d21983cd08c03309322babb35123ffeb3b7b92`.
Latest gameplay change package = deterministic early-game AI outcomes:
- Ladislaus Austria 4/4/4.
- AI Hungary strongly/deterministically routed to free Austrian PU via event choices; alternate leukemia bypass blocked for AI.
- AI Moldavia routed to Poland; Hungary/independence factors zero.
- England refuses Maine; France selects war; HYW CB declaration path preserved.

[PENDING RUNTIME TEST]
- Verify Austria/Hungary succession chain in actual campaign through event timing.
- Verify Moldavia chooses Poland in actual campaign.
- Verify Maine chain results in ENG-FRA Hundred Years War under normal trigger conditions.

[PENDING DESIGN]
- Future PAP work should start from Vanilla Papal preset and modify selectively. No PAP v2.2 custom tree currently active.

===============================================================================
END CANONICAL STATE
===============================================================================
