# Python files to control magnets via EPICS

* Vcorrectors.py, Hcorrector.py: adjust the steering magnets with sliders
* Magnets.py: adjust quadrupoles and solenoids
* Wien-filters.py: sets the spin rotation angles
* show_bpm.py: displays the beam positions
* quad_scan.py: varies a solenoid and analyzes the beam position change on a screen
* make_response_matrix.py: changes one steering magnet at a time and records the changes of the beam position
* correct_orbit.py: corrects the orbit using all correctors and all BPM
* SideBySide.py: allows to see and change the process variables of the twin and the accelerator side by side
