<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  
  

  


  

  <head>
    <title>
      /branches/funf_core_demo/res/raw/funf_db2csv.py –
      funf-os
    </title>
        <link rel="search" href="/funf-os/search" />
        <link rel="help" href="/funf-os/wiki/TracGuide" />
        <link rel="alternate" href="/funf-os/browser/branches/funf_core_demo/res/raw/funf_db2csv.py?format=txt" type="text/plain" title="Plain Text" /><link rel="alternate" href="/funf-os/export/67/branches/funf_core_demo/res/raw/funf_db2csv.py" type="text/x-python; charset=iso-8859-15" title="Original Format" />
        <link rel="up" href="/funf-os/browser/branches/funf_core_demo/res/raw" title="Parent directory" />
        <link rel="start" href="/funf-os/wiki" />
        <link rel="stylesheet" href="/funf-os/chrome/common/css/trac.css" type="text/css" /><link rel="stylesheet" href="/funf-os/chrome/common/css/code.css" type="text/css" /><link rel="stylesheet" href="/funf-os/pygments/trac.css" type="text/css" /><link rel="stylesheet" href="/funf-os/chrome/common/css/browser.css" type="text/css" />
        <link rel="shortcut icon" href="/funf-os/chrome/common/trac.ico" type="image/x-icon" />
        <link rel="icon" href="/funf-os/chrome/common/trac.ico" type="image/x-icon" />
      <link type="application/opensearchdescription+xml" rel="search" href="/funf-os/search/opensearch" title="Search funf-os" />
    <script type="text/javascript" src="/funf-os/chrome/common/js/jquery.js"></script><script type="text/javascript" src="/funf-os/chrome/common/js/trac.js"></script><script type="text/javascript" src="/funf-os/chrome/common/js/search.js"></script>
    <!--[if lt IE 7]>
    <script type="text/javascript" src="/funf-os/chrome/common/js/ie_pre7_hacks.js"></script>
    <![endif]-->
    <script type="text/javascript">
      jQuery(document).ready(function($) {
        $("#jumploc input").hide();
        $("#jumploc select").change(function () {
          this.parentNode.parentNode.submit();
        })
      });
    </script>
  </head>
  <body>
    <div id="banner">
      <div id="header">
        <a id="logo" href="/funf-os/wiki/TracIni#header_logo-section"><img src="/funf-os/chrome/site/your_project_logo.png" alt="(please configure the [header_logo] section in trac.ini)" /></a>
      </div>
      <form id="search" action="/funf-os/search" method="get">
        <div>
          <label for="proj-search">Search:</label>
          <input type="text" id="proj-search" name="q" size="18" value="" />
          <input type="submit" value="Search" />
        </div>
      </form>
      <div id="metanav" class="nav">
    <ul>
      <li class="first">logged in as codys@mit.edu</li><li><a href="/funf-os/logout">Logout</a></li><li><a href="/funf-os/prefs">Preferences</a></li><li><a href="/funf-os/wiki/TracGuide">Help/Guide</a></li><li class="last"><a href="/funf-os/about">About Trac</a></li>
    </ul>
  </div>
    </div>
    <div id="mainnav" class="nav">
    <ul>
      <li class="first"><a href="/funf-os/wiki">Wiki</a></li><li><a href="/funf-os/timeline">Timeline</a></li><li><a href="/funf-os/roadmap">Roadmap</a></li><li class="active"><a href="/funf-os/browser">Browse Source</a></li><li><a href="/funf-os/report">View Tickets</a></li><li><a href="/funf-os/newticket">New Ticket</a></li><li class="last"><a href="/funf-os/search">Search</a></li>
    </ul>
  </div>
    <div id="main">
      <div id="ctxtnav" class="nav">
        <h2>Context Navigation</h2>
          <ul>
            <li class="first "><a href="/funf-os/changeset/43/branches/funf_core_demo/res/raw/funf_db2csv.py">Last Change</a></li><li><a href="/funf-os/browser/branches/funf_core_demo/res/raw/funf_db2csv.py?annotate=blame&amp;rev=43" title="Annotate each line with the last changed revision (this can be time consuming...)">Annotate</a></li><li class="last"><a href="/funf-os/log/branches/funf_core_demo/res/raw/funf_db2csv.py">Revision Log</a></li>
          </ul>
        <hr />
      </div>
    <div id="content" class="browser">
      <h1>
    <a class="pathentry first" title="Go to root directory" href="/funf-os/browser">root</a><span class="pathentry sep">/</span><a class="pathentry" title="View branches" href="/funf-os/browser/branches">branches</a><span class="pathentry sep">/</span><a class="pathentry" title="View funf_core_demo" href="/funf-os/browser/branches/funf_core_demo">funf_core_demo</a><span class="pathentry sep">/</span><a class="pathentry" title="View res" href="/funf-os/browser/branches/funf_core_demo/res">res</a><span class="pathentry sep">/</span><a class="pathentry" title="View raw" href="/funf-os/browser/branches/funf_core_demo/res/raw">raw</a><span class="pathentry sep">/</span><a class="pathentry" title="View funf_db2csv.py" href="/funf-os/browser/branches/funf_core_demo/res/raw/funf_db2csv.py">funf_db2csv.py</a>
    <br style="clear: both" />
  </h1>
      <div id="jumprev">
        <form action="" method="get">
          <div>
            <label for="rev">
              View revision:</label>
            <input type="text" id="rev" name="rev" size="6" />
          </div>
        </form>
      </div>
      <div id="jumploc">
        <form action="" method="get">
          <div class="buttons">
            <label for="preselected">Visit:</label>
            <select id="preselected" name="preselected">
              <option selected="selected"></option>
              <optgroup label="branches">
                <option value="/funf-os/browser/trunk">trunk</option><option value="/funf-os/browser/branches/funf-davos">branches/funf-davos</option><option value="/funf-os/browser/branches/funf_core_april">branches/funf_core_april</option><option value="/funf-os/browser/branches/funf_core_demo">branches/funf_core_demo</option><option value="/funf-os/browser/branches/funf_website">branches/funf_website</option><option value="/funf-os/browser/branches/pds_project_snapshot">branches/pds_project_snapshot</option>
              </optgroup>
            </select>
            <input type="submit" value="Go!" title="Jump to the chosen preselected path" />
          </div>
        </form>
      </div>
      <table id="info" summary="Revision info">
        <tr>
          <th scope="col">
            Revision <a href="/funf-os/changeset/43">43</a>, <span title="2990 bytes">2.9 kB</span>
            (checked in by alan.gardner@…, <a class="timeline" href="/funf-os/timeline?from=2011-05-02T20%3A12%3A25Z-0400&amp;precision=second" title="2011-05-02T20:12:25Z-0400 in Timeline">6 days</a> ago)
          </th>
        </tr>
        <tr>
          <td class="message searchable">
              <p>
Have the db2csv python script be included in every data zip file, for user convenience.<br />
</p>
          </td>
        </tr>
      </table>
      <div id="preview" class="searchable">
    <table class="code"><thead><tr><th class="lineno" title="Line numbers">Line</th><th class="content"> </th></tr></thead><tbody><tr><th id="L1"><a href="#L1">1</a></th><td><span class="c">#!/usr/bin/env python</span></td></tr><tr><th id="L2"><a href="#L2">2</a></th><td><span class="sd">'''Merges data from a group of Funf sqlite files into one CSV file per table.</span></td></tr><tr><th id="L3"><a href="#L3">3</a></th><td><span class="sd">'''</span></td></tr><tr><th id="L4"><a href="#L4">4</a></th><td><span class="k">import</span> <span class="nn">sqlite3</span></td></tr><tr><th id="L5"><a href="#L5">5</a></th><td><span class="k">import</span> <span class="nn">csv</span><span class="o">,</span> <span class="nn">codecs</span><span class="o">,</span> <span class="nn">cStringIO</span></td></tr><tr><th id="L6"><a href="#L6">6</a></th><td><span class="k">from</span> <span class="nn">optparse</span> <span class="k">import</span> OptionParser</td></tr><tr><th id="L7"><a href="#L7">7</a></th><td><span class="k">import</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">os.path</span></td></tr><tr><th id="L8"><a href="#L8">8</a></th><td></td></tr><tr><th id="L9"><a href="#L9">9</a></th><td>tables_to_convert <span class="o">=</span> <span class="p">[</span><span class="s">'screen'</span><span class="p">,</span> <span class="s">'battery'</span><span class="p">,</span> <span class="s">'sensoracc'</span><span class="p">,</span> <span class="s">'bluetooth'</span><span class="p">,</span> <span class="s">'wifi'</span><span class="p">,</span> <span class="s">'location'</span><span class="p">]</span></td></tr><tr><th id="L10"><a href="#L10">10</a></th><td></td></tr><tr><th id="L11"><a href="#L11">11</a></th><td></td></tr><tr><th id="L12"><a href="#L12">12</a></th><td><span class="k">def</span> <span class="nf">csv_filepath</span><span class="p">(</span>out_dir<span class="p">,</span> table_name<span class="p">):</span></td></tr><tr><th id="L13"><a href="#L13">13</a></th><td>    <span class="k">return</span> os<span class="o">.</span>path<span class="o">.</span>join<span class="p">(</span>out_dir<span class="p">,</span> table_name <span class="o">+</span> <span class="s">".csv"</span><span class="p">)</span></td></tr><tr><th id="L14"><a href="#L14">14</a></th><td></td></tr><tr><th id="L15"><a href="#L15">15</a></th><td><span class="k">def</span> <span class="nf">convert</span><span class="p">(</span>db_files<span class="o">=</span><span class="bp">None</span><span class="p">,</span> out_dir<span class="o">=</span><span class="bp">None</span><span class="p">):</span></td></tr><tr><th id="L16"><a href="#L16">16</a></th><td>    <span class="c"># Check that db_files are specified and exist</span></td></tr><tr><th id="L17"><a href="#L17">17</a></th><td>    <span class="k">if</span> <span class="ow">not</span> db_files<span class="p">:</span></td></tr><tr><th id="L18"><a href="#L18">18</a></th><td>        db_files <span class="o">=</span> <span class="p">[</span><span class="nb">file</span> <span class="k">for</span> <span class="nb">file</span> <span class="ow">in</span> os<span class="o">.</span>listdir<span class="p">(</span>os<span class="o">.</span>curdir<span class="p">)</span> <span class="k">if</span> <span class="nb">file</span><span class="o">.</span>endswith<span class="p">(</span><span class="s">".db"</span><span class="p">)]</span></td></tr><tr><th id="L19"><a href="#L19">19</a></th><td>        <span class="k">if</span> <span class="ow">not</span> db_files<span class="p">:</span> </td></tr><tr><th id="L20"><a href="#L20">20</a></th><td>            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">"Must specify at least one db file"</span><span class="p">)</span></td></tr><tr><th id="L21"><a href="#L21">21</a></th><td>    nonexistent_files <span class="o">=</span> <span class="p">[</span><span class="nb">file</span> <span class="k">for</span> <span class="nb">file</span> <span class="ow">in</span> db_files <span class="k">if</span> <span class="ow">not</span> os<span class="o">.</span>path<span class="o">.</span>exists<span class="p">(</span><span class="nb">file</span><span class="p">)]</span></td></tr><tr><th id="L22"><a href="#L22">22</a></th><td>    <span class="k">if</span> nonexistent_files<span class="p">:</span></td></tr><tr><th id="L23"><a href="#L23">23</a></th><td>        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">"The following db files do not exist: </span><span class="si">%s</span><span class="s">"</span> <span class="o">%</span> nonexistent_files<span class="p">)</span></td></tr><tr><th id="L24"><a href="#L24">24</a></th><td>    </td></tr><tr><th id="L25"><a href="#L25">25</a></th><td>    <span class="c"># Create dir if not already created.  Default to current dir.</span></td></tr><tr><th id="L26"><a href="#L26">26</a></th><td>    <span class="k">if</span> out_dir<span class="p">:</span></td></tr><tr><th id="L27"><a href="#L27">27</a></th><td>        <span class="k">if</span> <span class="ow">not</span> os<span class="o">.</span>path<span class="o">.</span>exists<span class="p">(</span>out_dir<span class="p">):</span></td></tr><tr><th id="L28"><a href="#L28">28</a></th><td>            os<span class="o">.</span>makedirs<span class="p">(</span>out_dir<span class="p">)</span></td></tr><tr><th id="L29"><a href="#L29">29</a></th><td>    <span class="k">else</span><span class="p">:</span></td></tr><tr><th id="L30"><a href="#L30">30</a></th><td>        out_dir <span class="o">=</span> os<span class="o">.</span>curdir</td></tr><tr><th id="L31"><a href="#L31">31</a></th><td>    </td></tr><tr><th id="L32"><a href="#L32">32</a></th><td>    <span class="c"># Ensure CSV files don't already exist</span></td></tr><tr><th id="L33"><a href="#L33">33</a></th><td>    csv_files <span class="o">=</span> <span class="p">[</span>csv_filepath<span class="p">(</span>out_dir<span class="p">,</span> table<span class="p">)</span> <span class="k">for</span> table <span class="ow">in</span> tables_to_convert<span class="p">]</span></td></tr><tr><th id="L34"><a href="#L34">34</a></th><td>    existing_files <span class="o">=</span> <span class="p">[</span><span class="nb">file</span> <span class="k">for</span> <span class="nb">file</span> <span class="ow">in</span> csv_files <span class="k">if</span> os<span class="o">.</span>path<span class="o">.</span>exists<span class="p">(</span><span class="nb">file</span><span class="p">)]</span></td></tr><tr><th id="L35"><a href="#L35">35</a></th><td>    <span class="k">if</span> existing_files<span class="p">:</span></td></tr><tr><th id="L36"><a href="#L36">36</a></th><td>        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">"The following csv files already exist: </span><span class="si">%s</span><span class="s">.  </span><span class="se">\n</span><span class="s">Move or delete them, or use the -o option to write to another directory."</span> <span class="o">%</span> existing_files<span class="p">)</span></td></tr><tr><th id="L37"><a href="#L37">37</a></th><td>    </td></tr><tr><th id="L38"><a href="#L38">38</a></th><td>    </td></tr><tr><th id="L39"><a href="#L39">39</a></th><td>    <span class="c"># Loop over db files outputing to different csv file for each table</span></td></tr><tr><th id="L40"><a href="#L40">40</a></th><td>    <span class="k">for</span> db_file <span class="ow">in</span> db_files<span class="p">:</span></td></tr><tr><th id="L41"><a href="#L41">41</a></th><td>        conn <span class="o">=</span> sqlite3<span class="o">.</span>connect<span class="p">(</span>db_file<span class="p">)</span></td></tr><tr><th id="L42"><a href="#L42">42</a></th><td>        conn<span class="o">.</span>row_factory <span class="o">=</span> sqlite3<span class="o">.</span>Row</td></tr><tr><th id="L43"><a href="#L43">43</a></th><td>        cursor <span class="o">=</span> conn<span class="o">.</span>cursor<span class="p">()</span></td></tr><tr><th id="L44"><a href="#L44">44</a></th><td>        <span class="k">for</span> table <span class="ow">in</span> tables_to_convert<span class="p">:</span></td></tr><tr><th id="L45"><a href="#L45">45</a></th><td>            <span class="k">try</span><span class="p">:</span> </td></tr><tr><th id="L46"><a href="#L46">46</a></th><td>                cursor<span class="o">.</span>execute<span class="p">(</span><span class="s">"select * from </span><span class="si">%s</span><span class="s">"</span> <span class="o">%</span> table<span class="p">)</span></td></tr><tr><th id="L47"><a href="#L47">47</a></th><td>            <span class="k">except</span> sqlite3<span class="o">.</span>OperationalError<span class="p">:</span></td></tr><tr><th id="L48"><a href="#L48">48</a></th><td>                <span class="k">pass</span> <span class="c"># table doesn't exist, move on</span></td></tr><tr><th id="L49"><a href="#L49">49</a></th><td>            <span class="k">else</span><span class="p">:</span></td></tr><tr><th id="L50"><a href="#L50">50</a></th><td>                csv_file_path <span class="o">=</span> csv_filepath<span class="p">(</span>out_dir<span class="p">,</span> table<span class="p">)</span></td></tr><tr><th id="L51"><a href="#L51">51</a></th><td>                needs_header <span class="o">=</span> <span class="ow">not</span> os<span class="o">.</span>path<span class="o">.</span>exists<span class="p">(</span>csv_file_path<span class="p">)</span></td></tr><tr><th id="L52"><a href="#L52">52</a></th><td>                <span class="k">with</span> <span class="nb">open</span><span class="p">(</span>csv_file_path<span class="p">,</span> <span class="s">'ab'</span><span class="p">)</span> <span class="k">as</span> csv_file<span class="p">:</span></td></tr><tr><th id="L53"><a href="#L53">53</a></th><td>                    csv_writer <span class="o">=</span> csv<span class="o">.</span>writer<span class="p">(</span>csv_file<span class="p">)</span></td></tr><tr><th id="L54"><a href="#L54">54</a></th><td>                    <span class="k">for</span> row <span class="ow">in</span> cursor<span class="p">:</span></td></tr><tr><th id="L55"><a href="#L55">55</a></th><td>                        <span class="c"># Write header if it is the first line of the file</span></td></tr><tr><th id="L56"><a href="#L56">56</a></th><td>                        <span class="k">if</span> needs_header<span class="p">:</span></td></tr><tr><th id="L57"><a href="#L57">57</a></th><td>                            csv_writer<span class="o">.</span>writerow<span class="p">(</span>row<span class="o">.</span>keys<span class="p">())</span></td></tr><tr><th id="L58"><a href="#L58">58</a></th><td>                            needs_header <span class="o">=</span> <span class="bp">False</span></td></tr><tr><th id="L59"><a href="#L59">59</a></th><td>                        csv_writer<span class="o">.</span>writerow<span class="p">([</span><span class="nb">unicode</span><span class="p">(</span>column<span class="p">)</span><span class="o">.</span>encode<span class="p">(</span><span class="s">'utf-8'</span><span class="p">)</span> <span class="k">for</span> column <span class="ow">in</span> row<span class="p">])</span></td></tr><tr><th id="L60"><a href="#L60">60</a></th><td></td></tr><tr><th id="L61"><a href="#L61">61</a></th><td></td></tr><tr><th id="L62"><a href="#L62">62</a></th><td><span class="k">if</span> __name__ <span class="o">==</span> <span class="s">'__main__'</span><span class="p">:</span></td></tr><tr><th id="L63"><a href="#L63">63</a></th><td>    parser <span class="o">=</span> OptionParser<span class="p">(</span>usage<span class="o">=</span><span class="s">"usage: %prog [options] [sqlite_file1.db [sqlite_file2.db...]]"</span><span class="p">)</span></td></tr><tr><th id="L64"><a href="#L64">64</a></th><td>    parser<span class="o">.</span>add_option<span class="p">(</span><span class="s">"-o"</span><span class="p">,</span> <span class="s">"--output"</span><span class="p">,</span> dest<span class="o">=</span><span class="s">"directory"</span><span class="p">,</span> default<span class="o">=</span><span class="bp">None</span><span class="p">,</span></td></tr><tr><th id="L65"><a href="#L65">65</a></th><td>                      help<span class="o">=</span><span class="s">"Directory csv files will be sent to.  Created if it doesn't exist."</span><span class="p">,</span> metavar<span class="o">=</span><span class="s">"DIR"</span><span class="p">)</span></td></tr><tr><th id="L66"><a href="#L66">66</a></th><td>    <span class="p">(</span>options<span class="p">,</span> args<span class="p">)</span> <span class="o">=</span> parser<span class="o">.</span>parse_args<span class="p">()</span></td></tr><tr><th id="L67"><a href="#L67">67</a></th><td>    <span class="k">try</span><span class="p">:</span></td></tr><tr><th id="L68"><a href="#L68">68</a></th><td>        convert<span class="p">(</span>args<span class="p">,</span> options<span class="o">.</span>directory<span class="p">)</span></td></tr><tr><th id="L69"><a href="#L69">69</a></th><td>    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> e<span class="p">:</span></td></tr><tr><th id="L70"><a href="#L70">70</a></th><td>        <span class="k">import</span> <span class="nn">sys</span></td></tr><tr><th id="L71"><a href="#L71">71</a></th><td>        sys<span class="o">.</span>exit<span class="p">(</span><span class="s">"ERROR: "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span>e<span class="p">))</span></td></tr></tbody></table>
      </div>
      <div id="help">
        <strong>Note:</strong> See <a href="/funf-os/wiki/TracBrowser">TracBrowser</a>
        for help on using the browser.
      </div>
      <div id="anydiff">
        <form action="/funf-os/diff" method="get">
          <div class="buttons">
            <input type="hidden" name="new_path" value="/branches/funf_core_demo/res/raw/funf_db2csv.py" />
            <input type="hidden" name="old_path" value="/branches/funf_core_demo/res/raw/funf_db2csv.py" />
            <input type="hidden" name="new_rev" value="43" />
            <input type="hidden" name="old_rev" value="43" />
            <input type="submit" value="View changes..." title="Select paths and revs for Diff" />
          </div>
        </form>
      </div>
    </div>
    <div id="altlinks">
      <h3>Download in other formats:</h3>
      <ul>
        <li class="first">
          <a rel="nofollow" href="/funf-os/browser/branches/funf_core_demo/res/raw/funf_db2csv.py?format=txt">Plain Text</a>
        </li><li class="last">
          <a rel="nofollow" href="/funf-os/export/67/branches/funf_core_demo/res/raw/funf_db2csv.py">Original Format</a>
        </li>
      </ul>
    </div>
    </div>
    <div id="footer" lang="en" xml:lang="en"><hr />
      <a id="tracpowered" href="http://trac.edgewall.org/"><img src="/funf-os/chrome/common/trac_logo_mini.png" height="30" width="107" alt="Trac Powered" /></a>
      <p class="left">
        Powered by <a href="/funf-os/about"><strong>Trac 0.11.1</strong></a><br />
        By <a href="http://www.edgewall.org/">Edgewall Software</a>.
      </p>
      <p class="right">Visit the Trac open source project at<br /><a href="http://trac.edgewall.org/">http://trac.edgewall.org/</a></p>
    </div>
  </body>
</html>