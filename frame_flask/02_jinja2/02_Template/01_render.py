# encoding:utf-8
'''
Template����Ա�������һ���������ģ���ļ�������������Ŀ���ı�.

Template��Ĺ�����������Environment�������ͬ, �����ǣ�����Templateʵ����Ҫһ��ģ���ı�����������������Ҫloader������
Templateʵ����һ�����ɱ���󣬼��㲻���޸�Templateʵ�������ԡ�

һ������£����ǻ�ʹ��Environmentʵ��������Template����Ҳ����ֱ��ʹ��Template�����������������Ҫ�ù��������� ��Templateʵ������ôJinja����ݹ����������Զ�Ϊ��Template����/ָ��һ���ڲ�Environmentʵ��������ʹ����ͬ�������� ��(������ģ���ı�������)������Templateʵ�����Ṳ��ͬһ���ڲ�Environmentʵ���� 
'''

from jinja2 import Template

'''
������<pre>render(*args, **kwargs)</pre> 
�˷��������롰dict����ͬ�Ĺ�����������һ��dict�����࣬����һЩ�ؼ��ֲ�����
'''

template = Template('Hello {{ name }}!')
print template.render(name='World')
template = Template('{{ knights }}!')
print template.render({'knights': 'that say nih'})
'''
ͨ������һ��Template��ʵ�������õ�һ���µ�ģ������ṩһ����Ϊrender()�ķ������÷��������ֵ��ؼ��ֲ���ʱ��������ģ�塣�ֵ��ؼ��ֲ����ᱻ���ݵ�ģ�壬��ģ�塰�����ġ���
'''
