import math,itertools
from .common import number,integer,identifier
def run(d):
 names=d['factors'];design=d['runs'];order=integer(d.get('max_order',2),1,3)
 if not 1<=len(names)<=10 or len(set(names))!=len(names)or not 1<=len(design)<=256:raise ValueError('design')
 for n in names:identifier(n)
 if any(len(r)!=len(names)or any(type(v)is not int or v not in [-1,1]for v in r)for r in design):raise ValueError('levels')
 cols={'I':[1]*len(design)}
 for k in range(1,min(order,len(names))+1):
  for combo in itertools.combinations(range(len(names)),k):cols['*'.join(names[i]for i in combo)]=[math.prod(r[i]for i in combo)for r in design]
 aliases=[];correlations=[]
 for a,b in itertools.combinations(cols,2):
  dot=sum(x*y for x,y in zip(cols[a],cols[b]))/len(design)
  if abs(dot)==1:aliases.append(dict(left=a,right=b,sign=int(dot)))
  elif dot!=0:correlations.append(dict(left=a,right=b,normalized_dot=dot))
 return dict(exact_aliases=aliases,partial_nonorthogonality=correlations,columns=len(cols),runs=len(design),duplicate_runs=len(design)-len({tuple(r)for r in design}))
