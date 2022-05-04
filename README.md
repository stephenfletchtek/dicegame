# dicegame project
<h2>Object oriented python</h2>
<p>This dice game was developed from an 'object oriented python' tutorial.</p>
<h2>To play the game</h2>
<p>Run 'dbgame.py' to play the game.</p>
<p>It has a simple menu driven user interface that allows a single player to roll dice, reroll & score much like the UK version of 'Yahtzee'.</p>
<h2>The files</h2>
<h3>dice.py</h3>
<p>The dice object and D6 were created during the tutorial to provide a 6-sided dice object for use in dice games.</p>
<h3>hands.py</h3>
<p>This creates a 'hand' object that holds 5 dice.</p>
<h3>reroll.py</h3>
<p>This places previously rolled dice into a hand and allows selected dice to be rerolled.</p>
<h3>scoresheets.py</h3>
<p>This evaluates a score for any given 'hand' or reroll hand.</p>
<h3>dbgame.py</h3>
<p>This file interacts with all of those listed above plus 'yahtzee.db' to provide the full 1-player game.</p>
<h3>Other files</h3>
<ul>
<li>'game.py' is a test game to check components are working - it doesn't keep the scores</li>
<li>'auto.py' is a simple experiment with automatic scoring and could be further developed as a 'computer' player</li>
<li>'yahtzee.db' is the sqlite database used to keep scores in 'dbgame.py'</li>
<li>'tests.py' contains units tests to check 'dice.py'</li>
</ul>
