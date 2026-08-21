import math
from math import sqrt, erf

def z(p):  # inverse normal via bisection
    lo,hi=-8.0,8.0
    for _ in range(200):
        mid=(lo+hi)/2
        c=0.5*(1+erf(mid/sqrt(2)))
        if c<p: lo=mid
        else: hi=mid
    return (lo+hi)/2

za=z(0.975)   # two-sided 0.05
za1=z(0.95)   # one-sided 0.05
def zb(power): return z(power)

print("="*74)
print("H1  PRIMARY: within-subject paired contrast (affected site vs upper abdomen)")
print("    Paired comparison of a sparkle metric. Effect = Cohen's dz.")
print("="*74)
print(f"{'dz':>6} {'80% power':>11} {'90% power':>11} {'90%+Bonf(5)':>13}")
# Bonferroni for 5 co-primary sparkle metrics -> alpha 0.01 two-sided
zab=z(1-0.01/2)
for dz in [0.4,0.5,0.6,0.8,1.0,1.2]:
    n80=(za+zb(0.80))**2/dz**2
    n90=(za+zb(0.90))**2/dz**2
    n90b=(zab+zb(0.90))**2/dz**2
    print(f"{dz:>6.1f} {math.ceil(n80):>11} {math.ceil(n90):>11} {math.ceil(n90b):>13}")
print("  Wilcoxon signed-rank fallback: inflate by ~1/0.955 (ARE) ~ +5%.")
print("  A 'casually visible' phenomenon implies dz well above 0.8;")
print("  powering at dz=0.5 (moderate) is deliberately conservative.")

print()
print("="*74)
print("H2  Between-group discrimination (lipoedema vs each control arm), AUC")
print("    Hanley-McNeil SE, balanced groups, precision (CI half-width) framing")
print("="*74)
def n_per_group_auc(A, hw, zc=za):
    Q1=A/(2-A); Q2=2*A*A/(1+A); a=A*(1-A); b=(Q1-A*A)+(Q2-A*A)
    t=(hw/zc)**2
    return (b+sqrt(b*b+4*t*(a-b)))/(2*t)
print(f"{'AUC':>6} {'+/-0.075':>10} {'+/-0.05':>10}")
for A in [0.75,0.80,0.85,0.90]:
    print(f"{A:>6.2f} {math.ceil(n_per_group_auc(A,0.075)):>10} {math.ceil(n_per_group_auc(A,0.05)):>10}")

print()
print("  Power to reject AUC=0.5 (existence of discrimination), per group:")
def n_power_auc(A, power=0.90, zc=za1):
    # variance of AUC under H1 (Hanley-McNeil) approx; null var uses A=0.5
    Q1=A/(2-A); Q2=2*A*A/(1+A)
    def var(a,n): return (a*(1-a)+(n-1)*(Q1_-a*a)+(n-1)*(Q2_-a*a))/(n*n) if False else None
    # Use Obuchowski approximate: n = ( za*sqrt(V0) + zb*sqrt(VA) )^2 / (A-0.5)^2, per group with VA in terms of variance function *n
    # variance function form: Var = [ A(1-A) + (n-1)(Q1-A^2) + (n-1)(Q2-A^2) ] / n^2  (equal n per group)
    for n in range(4,400):
        VA=(A*(1-A)+(n-1)*(Q1-A*A)+(n-1)*(Q2-A*A))/(n*n)
        # null
        A0=0.5; Q10=A0/(2-A0); Q20=2*A0*A0/(1+A0)
        V0=(A0*(1-A0)+(n-1)*(Q10-A0*A0)+(n-1)*(Q20-A0*A0))/(n*n)
        stat=(A-0.5)/sqrt(VA)
        # power = P(Z > za1*sqrt(V0/VA) - (A-.5)/sqrt(VA))
        thr=zc*sqrt(V0)/sqrt(VA) - (A-0.5)/sqrt(VA)
        pw=1-0.5*(1+erf(thr/sqrt(2)))
        if pw>=power:
            return n
    return None
for A in [0.70,0.75,0.80]:
    n=n_power_auc(A)
    print(f"    AUC {A:.2f}: ~{n}/group for 90% power (one-sided 0.05)")

print()
print("="*74)
print("H4  Independent TEST cohort: precision of the frozen-model AUC")
print("="*74)
for A in [0.80,0.85]:
    for hw in [0.075,0.10]:
        n=math.ceil(n_per_group_auc(A,hw))
        print(f"    AUC {A:.2f} +/- {hw}: {n}/class -> {2*n} test subjects")

print()
print("="*74)
print("H3  Ultrasound-histology correlation (liposuction sub-study), Pearson r")
print("="*74)
def n_corr(r, power=0.80, zc=za):
    zr=0.5*math.log((1+r)/(1-r))
    return ((zc+zb(power))/zr)**2 + 3
for r in [0.4,0.5,0.6]:
    print(f"    detect r={r}: n~{math.ceil(n_corr(r))} biopsy-scan pairs (80% power)")

print()
print("="*74)
print("RECRUITMENT ROLL-UP (with attrition and console stratification)")
print("="*74)
# Drivers: H2 AUC0.80 +/-0.075 per group; H1 paired dz0.5 90%; test cohort separate
h2=math.ceil(n_per_group_auc(0.80,0.075))
h1=math.ceil((za+zb(0.90))**2/0.5**2)
print(f"  H1 paired (dz=0.5, 90%): {h1} lipoedema participants")
print(f"  H2 per-arm (AUC0.80 +/-0.075): {h2}/arm")
print(f"  Binding development-cohort driver per arm: {max(h1,h2)}")
dev=max(h1,h2)
print(f"  Dev cohort, 5 arms: ~{dev*5} ; +15% attrition: ~{math.ceil(dev*5*1.15)}")
test=math.ceil(n_per_group_auc(0.80,0.10))
print(f"  Independent TEST cohort (AUC0.80 +/-0.10): {test}/class x2 = {test*2}; +15%: {math.ceil(test*2*1.15)}")
print(f"  Histology sub-study: ~{math.ceil(n_corr(0.5))} liposuction participants (subset of lipoedema arm)")
