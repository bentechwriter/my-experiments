<h1>Heading 1</h1>

<p>A sentence in p elements.</p>

Code using markdown indent:

    x = y * 2

Code using pre and code elements:

<pre><code>x = y * 2</code></pre>

A sentence with a span: <span class="unknown_class">this is inside a span element</span>.

An admonition with html:

<div class="unknown_class'>>
  <p class="unknown_class'>Admonition title
  </p>
  <p>Admonition text.
  </p>
</div>
                          
Admonitions with GitHub markdown:                          
                          
> **WARNING**: Be careful!

| Be careful |

| WARNING: be careful! |
| --- |

| **WARNING**: be careful! |
| --- |

Markdown simple list with code:

* One

        x = y * 3
    
* Two
* Three

Markdown nested list with code:

* Item 1

    * One

            x = y * 3

    * Two
    * Three

* Item 2
* Item 3

Simple list with ul li elements:

<ul>
  <li>One
  </li>
  <li>Two
  </li>
  <li>Three
  </li>
</ul>

Simple list with  ul li pre code elements:

<ul>
  <li>One
  <pre><code>z = x * y</code></pre>
  </li>
  <li>Two
  </li>
  <li>Three
  </li>
</ul>

Simple list with CSS:

<ul>
  <li>One
  <pre><code class="unknown_style">z = x * y</code></pre>
  </li>
  <li>Two
  </li>
  <li>Three
  </li>
</ul>


Nested list with ul li pre codeelements:

<ol>
  <li>
    <ul>
      <li>One
        <pre><code>z = x * y</code></pre>
      </li>
      <li>Two
      </li>
      <li>Three
      </li>
    </ul>
  </li>
  <li>
    <ul>
      <li>Four
      </li>
      <li>Five
      </li>
      <li>Six
      </li>
    </ul>
  </li>
</ol>
