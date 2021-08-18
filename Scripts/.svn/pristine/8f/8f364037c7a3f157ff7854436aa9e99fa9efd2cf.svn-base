#to open a widget library tcl and get the widgets description by difference way

from pprint import pprint
import re

with open('A661WL_GpLine.tcl') as f:
	content = f.read()
	
block_widgets = re.search(r'# 3. Widgets description #(.*?#END)', content, re.S).group(1).strip()

# Method 1
for line in re.findall(r'^#\s*\d+.*?(?=#END|^#\s*\d+)', block_widgets, re.S|re.M):
	line = re.sub(r'[\r\n]#\s+', ' ', line.strip())
	# Process Line
	#...

# Method 2
lines = list()
for line in block_widgets.splitlines():
	line = line.lstrip('#').strip()
	if re.match('END', line):
		continue
	elif re.match('\d+', line):
		lines.append(line)
	else:
		lines[-1] += line
		
for l in lines:
	pass
	# Process Line
	#...

	
# Method 3
list_widg = list()
for l in block_widgets.splitlines():
	l = l.lstrip('#').strip()
	m_widg = re.match(r'(\d+(?:@\d+)?)\s+(\w+)\s+(.*)', l)
	if re.match('END', l):
		continue
	elif m_widg:
		list_widg.append({
			'id':m_widg.group(1),
			'name':m_widg.group(2),
			'descr':m_widg.group(3),
		})
	else:
		list_widg[-1]['descr'] += l

print(list_widg)