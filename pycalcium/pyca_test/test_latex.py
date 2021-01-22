latex_test_cases = [
    ("""f(0)""", "f(0)"),
    ("""f("Hello, world!")""", "f(\\text{``Hello, world!''})"),
    ("f", r"f"),
    ("f_", r"f"),
    ("f_(0)", r"f_{0}"),
    ("f()", r"f()"),
    ("Add(Add(Add(f(a, b), c_(n)), f_(x, y)), f_())", r"f(a, b) + c_{n} + f_{x, y} + f_{}"),
    ("f(a)(b)", r"f(a)(b)"),
    ("Mul(f, g)(x)", r"\left(f g\right)(x)"),
    ("Add(f, g)(x)", r"\left(f + g\right)(x)"),
    ("c_(m, n, p)(x, y, z)", r"c_{m, n, p}(x, y, z)"),
    ("f_(Div(-3, 2))(Div(-3, 2))", r"f_{-3 / 2}\!\left(-\frac{3}{2}\right)"),
    ("Mul(2, Pi, NumberI)", r"2 \pi i"),
    ("Mul(-2, Pi, NumberI)", r"-2 \pi i"),
    ("Add(2, x)", r"2 + x"),
    ("Sub(2, x)", r"2 - x"),
    ("Add(2, Neg(x))", r"2 + \left(-x\right)"),
    ("Sub(2, Neg(x))", r"2 - \left(-x\right)"),
    ("Add(2, Sub(x, y))", r"2 + \left(x - y\right)"),
    ("Sub(2, Add(x, y))", r"2 - \left(x + y\right)"),
    ("Sub(2, Sub(x, y))", r"2 - \left(x - y\right)"),
    ("Add(-3, -4, -5)", r"-3-4-5"),
    ("Add(-3, Mul(-4, x), -5)", r"-3-4 x-5"),
    ("Add(-3, Mul(-4, x), Pos(5))", r"-3-4 x+5"),
    ("Add(-3, Div(Mul(-4, x), 7), -5)", r"-3-\frac{4 x}{7}-5"),
    ("Add(-3, Div(Mul(4, x), 7), -5)", r"-3 + \frac{4 x}{7}-5"),
    ("Mul(0, 1)", r"0 \cdot 1"),
    ("Mul(3, Pow(2, n))", r"3 \cdot {2}^{n}"),
    ("Mul(3, Pow(-1, n))", r"3 \cdot {\left(-1\right)}^{n}"),
    ("Mul(-3, Pow(-1, n))", r"-3 \cdot {\left(-1\right)}^{n}"),
    ("Mul(-1, -2, -3)", r"-1 \cdot \left(-2\right) \cdot \left(-3\right)"),
    ("Div(-1, 3)", r"-\frac{1}{3}"),
    ("Div(Mul(-5, Pi), 3)", r"-\frac{5 \pi}{3}"),
    ("Div(Neg(Mul(5, Pi)), 3)", r"-\frac{5 \pi}{3}"),
    ("Div(Add(Add(Mul(-5, Pow(x, 2)), Mul(4, x)), 1), Add(Mul(3, x), y))", r"\frac{-5 {x}^{2} + 4 x + 1}{3 x + y}"),
    ("Pow(2, n)", r"{2}^{n}"),
    ("Pow(-1, n)", r"{\left(-1\right)}^{n}"),
    ("Pow(10, Pow(10, -10))", r"{10}^{{10}^{-10}}"),
    ("Pow(2, Div(-1, 3))", r"{2}^{-1 / 3}"),
    ("Pow(2, Div(-1, Mul(3, n)))", r"{2}^{-1 / \left(3 n\right)}"),
    ("Equal(Add(Pow(Sin(x), 2), Pow(Cos(x), 2)), 1)", r"\sin^{2}\!\left(x\right) + \cos^{2}\!\left(x\right) = 1"),
    ("Subset(Primes, NN, ZZ, QQ, RR, CC)", r"\mathbb{P} \subset \mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}"),
    ("Subset(QQ, AlgebraicNumbers, CC)", r"\mathbb{Q} \subset \overline{\mathbb{Q}} \subset \mathbb{C}"),
    ("SubsetEqual(S, QQ)", r"S \subseteq \mathbb{Q}"),
    ("Sum(f(n) + g(n), For(n, a, b))", r"\sum_{n=a}^{b} \left(f(n) + g(n)\right)"),
    ("Sum(f(n), For(n, ZZ))", r"\sum_{n  \in \mathbb{Z}} f(n)"),
    ("Sum(f(n), For(n, ZZ), NotEqual(n, 0))", r"\sum_{\textstyle{n  \in \mathbb{Z} \atop n \ne 0}} f(n)"),
    ("Sum(f(n), For(n, a, b), NotEqual(n, 0))", r"\sum_{\textstyle{n=a \atop n \ne 0}}^{b} f(n)"),
    ("Sum(f(n), For(n, a, b))", r"\sum_{n=a}^{b} f(n)"),
    ("Product(f(n) + g(n), For(n, a, b))", r"\prod_{n=a}^{b} \left(f(n) + g(n)\right)"),
    ("Product(f(n), For(n, NN))", r"\prod_{n  \in \mathbb{N}} f(n)"),
    ("Product(f(n), For(n, NN), NotEqual(g(n), 0))", r"\prod_{\textstyle{n  \in \mathbb{N} \atop g(n) \ne 0}} f(n)"),
    ("Product(f(n), For(n, a, b), NotEqual(n, 0))", r"\prod_{\textstyle{n=a \atop n \ne 0}}^{b} f(n)"),
    ("Product(f(n), For(n, a, b))", r"\prod_{n=a}^{b} f(n)"),
    ("Integral(f(x), For(x, -Infinity, Infinity))", r"\int_{-\infty}^{\infty} f(x) \, dx"),
    ("Integral(f(x), For(x, RR))", r"\int_{x \in \mathbb{R}} f(x) \, dx"),
    ("Integral(f(x) + g(x) / h(x), For(x, a, b))", r"\int_{a}^{b} \left(f(x) + \frac{g(x)}{h(x)}\right) \, dx"),
    ("Add(Sin(x), Cos(x), Tan(x), Cot(x), Sec(x), Csc(x))", r"\sin(x) + \cos(x) + \tan(x) + \cot(x) + \sec(x) + \csc(x)"),
    ("Add(Sinh(x), Cosh(x), Tanh(x), Coth(x), Sech(x), Csch(x))", r"\sinh(x) + \cosh(x) + \tanh(x) + \coth(x) + \operatorname{sech}(x) + \operatorname{csch}(x)"),
    ("Add(Asin(x), Acos(x), Atan(x), Acot(x), Asec(x), Acsc(x))", r"\operatorname{asin}(x) + \operatorname{acos}(x) + \operatorname{atan}(x) + \operatorname{acot}(x) + \operatorname{asec}(x) + \operatorname{acsc}(x)"),
    ("Add(Asinh(x), Acosh(x), Atanh(x), Acoth(x), Asech(x), Acsch(x))", r"\operatorname{asinh}(x) + \operatorname{acosh}(x) + \operatorname{atanh}(x) + \operatorname{acoth}(x) + \operatorname{asech}(x) + \operatorname{acsch}(x)"),
    ("Equal(RiemannZeta(s), Mul(Mul(Mul(Mul(2, Pow(Mul(2, Pi), Sub(s, 1))), Sin(Div(Mul(Pi, s), 2))), Gamma(Sub(1, s))), RiemannZeta(Sub(1, s))))", r"\zeta(s) = 2 {\left(2 \pi\right)}^{s - 1} \sin\!\left(\frac{\pi s}{2}\right) \Gamma\!\left(1 - s\right) \zeta\!\left(1 - s\right)"),
    ("Mul(Mul(Erf(z), Erfc(z)), Erfi(z))", r"\operatorname{erf}(z) \operatorname{erfc}(z) \operatorname{erfi}(z)"),
    ("Mul(EllipticK(m), EllipticE(m), EllipticPi(n, m))", r"K(m) E(m) \Pi(n, m)"),
    ("Mul(IncompleteEllipticE(z, m), IncompleteEllipticF(z, m), IncompleteEllipticPi(n, z, m))", r"E(z, m) F(z, m) \Pi(n, z, m)"),
    ("Add(CarlsonRF(x, y, z), CarlsonRG(x, y, z), CarlsonRJ(x, y, z, w), CarlsonRD(x, y, z), CarlsonRC(x, y))", r"R_F(x, y, z) + R_G(x, y, z) + R_J(x, y, z, w) + R_D(x, y, z) + R_C(x, y)"),
    ("Mul(Hypergeometric0F1(b, z), Hypergeometric0F1Regularized(b, z))", r"\,{}_0F_1(b, z) \,{}_0{\textbf F}_1(b, z)"),
    ("Mul(Hypergeometric1F1(a, b, z), Hypergeometric1F1Regularized(a, b, z))", r"\,{}_1F_1(a, b, z) \,{}_1{\textbf F}_1(a, b, z)"),
    ("Hypergeometric2F0(a, b, z)", r"\,{}_2F_0(a, b, z)"),
    ("Mul(HypergeometricU(a, b, z), HypergeometricUStar(a, b, z))", r"U(a, b, z) U^{*}(a, b, z)"),
    ("Mul(Hypergeometric2F1(a, b, c, z), Hypergeometric2F1Regularized(a, b, c, z))", r"\,{}_2F_1(a, b, c, z) \,{}_2{\textbf F}_1(a, b, c, z)"),
    ("Mul(Hypergeometric1F2(a, b, c, z), Hypergeometric1F2Regularized(a, b, c, z))", r"\,{}_1F_2(a, b, c, z) \,{}_1{\textbf F}_2(a, b, c, z)"),
    ("Mul(Hypergeometric2F2(a, b, c, d, z), Hypergeometric2F2Regularized(a, b, c, d, z))", r"\,{}_2F_2(a, b, c, d, z) \,{}_2{\textbf F}_2(a, b, c, d, z)"),
    ("Mul(Hypergeometric3F2(a, b, c, d, e, z), Hypergeometric3F2Regularized(a, b, c, d, e, z))", r"\,{}_3F_2(a, b, c, d, e, z) \,{}_3{\textbf F}_2(a, b, c, d, e, z)"),
    ("(Hypergeometric2F1Regularized(Div(-1,4),Div(1,4),1/2, (x-1)/2)**2)", r"{\left(\,{}_2{\textbf F}_1\!\left(-\frac{1}{4}, \frac{1}{4}, \frac{1}{2}, \frac{x - 1}{2}\right)\right)}^{2}"),
]

def test_latex(fexpr):
    print("test latex!")
    fexpr.inject(vars=True)
    for formula, expected in latex_test_cases:
        expr = eval(formula)
        latex = expr.latex()
        if latex != expected:
            raise AssertionError("%s:  got '%s', expected '%s'" % (formula, latex, expected))

def latex_report(fexpr):
    fexpr.inject(vars=True)
    formulas = [eval(formula) for formula, expected in latex_test_cases]
    from os.path import expanduser
    from time import clock
    fp = open(expanduser("~/Desktop/latex_report.html"), "w")
    fp.write("""
<!DOCTYPE html>
<html>
<head>
<title>Fredrik Johansson's website</title>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
tt { padding: 0.1em; background-color: #f8f8f8; border:1px solid #eee; }
table { border-collapse:collapse; margin: 1em; }
table, th, td { border: 1px solid #aaa; }
th, td { padding:0.1em 0.3em 0.1em 0.3em; }
table { width: 95%; }
.katex { font-size: 1.1em !important; } 
.katex-display { margin:0.1em; padding:0.1em; }
</style>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.css" integrity="sha384-AfEj0r4/OFrOo5t7NnNe46zW/tFgW6x/bCJG8FqQCEo3+Aro6EYUG4+cU+KJWu/X" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.js" integrity="sha384-g7c+Jr9ZivxKLnZTDUhnkOnsh30B4H0rpLUpJ4jAIKs4fnJI+sEnkvrMWph2EDg4" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/contrib/auto-render.min.js" integrity="sha384-mll67QQFJfxn0IYznZYonOWZ644AWYC+Pt2cHqMaRhXVrursRwvLnLaebdGIlYNa" crossorigin="anonymous"
    onload="renderMathInElement(document.body);"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
      renderMathInElement(document.body, {
          delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false}
          ]
      });
  });
</script>
</head>
<body>
""")
    output = [formula.latex() for formula in formulas]
    one_big = fexpr("BigLatex")(*formulas)
    t1 = clock()
    one_big_latex = one_big.latex()
    t2 = clock()
    fp.write("""<h1>fexpr to LaTeX test sheet</h1>""")
    fp.write("""<p>Converted %i formulas to LaTeX in %f seconds.</p>""" % (len(formulas), (t2-t1)))
    fp.write("""<table>""")
    fp.write("""<tr><th>fexpr</th> <th>Generated LaTeX</th> <th>KaTeX display</th>""")
    for formula, latex in zip(formulas, output):
        fp.write("""<tr>""")
        fp.write("""<td><tt>%s</tt></td>""" % formula)
        fp.write("""<td><tt>%s</tt></td>""" % latex)
        fp.write("""<td>$$%s$$</td>""" % latex)
        fp.write("""</tr>""")
    fp.write("""</table>""")

    fp.write("""<br/><p>Untested builtins:</p> <p><tt>""")
    s = str(one_big)
    for c in '-+()_,"':
        s = s.replace(c, " ")
    used = set(s.split())
    builtins = fexpr.builtins()
    unused = [name for name in builtins if name not in used]
    for name in unused:
        fp.write(name)
        fp.write(" ")
    fp.write("""</tt></p>""")
    fp.write("""</body></html>""")
    fp.close()
