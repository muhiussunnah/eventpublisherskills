# Hidden (unpublished) events — 2026-10-19

The dashboard has no per-event publish switch: an event's "Published" = its venue's `isPublished`.
To unpublish single events without hiding family events at the same venue, they were moved to an
**unpublished holding venue** ("[Dold] <venue> – ej familjeinnehåll", same organizer). Nothing was deleted.

**To re-publish an event:** PATCH the event with `placeId` = the original venue below (full body, see
technical-patterns.md "Image quality sweep" → PATCH body rules).

## Closed / non-existent places — venue unpublished (own venue, no other events)
| Event | Event ID | Venue (unpublished) | Reason |
|---|---|---|---|
| Vasalundshallen | 445128704851477680 | 445128692151125167 | Pool closed 2022 (Solna Simhall replaced it) |
| Tolvåkerbadet | 436014765366609100 | 436014761851782347 | Closed 30 Jun 2023 (Harjagersbadet replaced it) |
| Aqua Nova (Örebro) | 441696271703508349 | 441696259414197628 | No such public venue; aqua-nova.se is a lab-equipment company |

## Adult-only events — moved to holding venues
| Holding venue (unpublished) | Original venue | Events |
|---|---|---|
| 475592226836087960 | 225893969131767769 Ticketmaster Sverige | Ringmasters firar 20 år! (434922809903319019) |
| 475592246557705369 | 340726476989039971 Huddinge Kulturhus | Christina Gustafsson och Leo Lindbergs Trio (372741036637718521), Karl Olandersson kvartett (372741008451995531), Nils Ferlin och KlaraBohemerna (372740992094209821) |
| 475592282393838746 | 186703520404113140 Cirkus Cirkör | Blåsväder (372717466058524442), Marklyft (372717454314473135) |
| 475592309237384347 | 253061553203480491 Stadsbiblioteket (UKK/Uppsala) | Elton John meets Freddie Mercury (370749820584887912), Viktor Norén & Linus Wahlgren (370749792030066258), Grymlings (370749761386481212), Lisa Nilsson möter Bohuslän Big Band (370749711725921808), Ana Moura (370749687130523130), Christoffer Nyqvist (370749645707576804), Maksim (370749620818576846), Niklas Strömstedt (370749243893253560), The Simon & Garfunkel Story (370749193754543522), Elvis, Elvis, Elvis! på UKK (370749136980444534), Thomas Järvheden (370749099139433824), Weeping Willows Christmas (370749076590855498), Seinabo Sey (370748729646417182), Arvingarna (370748702341498120), West Of Eden (370748682728932594), Christmas in Ireland (370747290790429718), Doktor Glas (370745535826527618) |
| 475592446500177052 | 340079965687022763 Nynäshamn general venue | Utbildning Lymfmassör steg 2 (370568075705091211) |
| 475592466356012189 | 349420619902781198 Nya Cirkus | Elvis, Elvis, Elvis! - 2026 (349435204403758938) |
| 475592486144738462 | 247943996549137697 Kultur Upplands-Bro | Retroklubben (247949370056541475), Kulturklubben (247947080545371426) |

Total hidden: 30 events (3 closed places + 27 adult events). All original venues stay published, so the family
events there (Aladdin, LasseMaja, HippHipp, Labero, Babblarna, Bamse …) are unaffected.
`GET /admin/events?isEnd=false` still counts hidden events (1460 on 2026-10-19) — published live = 1430.
