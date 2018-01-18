#!usr/bin/python
#-*-encoding:utf-8-*-

P_RIGHT = [19,23,27,38,41,44,57,58,65,69,73,77]
P_WRONG = [2,8,10,17,33,50,62,80]

E_RIGHT = [1,5,9,13,16,22,29,32,35,40,43,46,49,53,56,61,72,76,85]
E_WRONG = [26,37]

N_RIGHT = [3,6,11,14,18,20,24,28,30,34,36,42,47,51,54,59,63,66,67,70,74,78,82,84]
N_WRONG = []

L_RIGHT = [12,31,48,68,79,81]
L_WRONG = [4,7,15,21,25,39,45,52,55,60,64,71,75,83]

theme = [
'1.你是否有广泛的爱好？',
'2.在做任何事情之前，你是否都要考虑一番？',
'3.你的情绪时常波动吗？',
'4.当别人做了好事，而周围的人认为是你做的时候，你是否感到洋洋得意？',
'5.你是一个健谈的人吗？',
'6.你曾经无缘无故地觉得自己“可怜”吗？',
'7.你曾经有过贪心使自己多得份外的物质利益吗?',
'8.晚上你是否小心地把门锁好？',
'9.你认为自己活泼吗？',
'10.当你看到小孩（或动物）受折磨时是否感到难受？',
'11.你是否常担心你会说出（或做出）不应该说或做的事?',
'12.若你说过要做某件事，是否不管遇到什么困难都要把它做成？',
'13.在愉快的聚会中你是否通常尽情享受？',
'14. 你是一位易激怒的人吗？',
'15.你是否有过自己做错了事反倒责备别人的时候？',
'16.你喜欢会见陌生人吗？',
'17.你是否相信参加储蓄是一种好办法？',
'18.你的感情是否容易受到伤害？',
'19.你是否服用有奇特效果或是有危险性的药物？',
'20.你是否时常感到“极其厌烦”？',
'21.你曾多占多得别人的东西（甚至一针一线）吗？',
'22.如果条件允许，你喜欢经常外出（旅行）吗？',
'23.对你所喜欢的人，你是否为取乐开过过头的玩笑？',
'24.你是否常因“自罪感”而烦恼？',
'25.你是否有时候谈论一些你毫无所知的事情？',
'26.你是否宁愿看些书，而不想去会见别人？',
'27.有坏人想要害你吗？',
'28.你认为自己“神经过敏”吗？',
'29.你的朋友多吗？',
'30.你是个忧虑重重的人吗？',
'31.你在儿童时代是否立即听从大人的吩咐而毫无怨言？',
'32.你是一个无忧无虑逍遥自在的人吗？',
'33.有礼貌爱整洁对你很重要吗？',
'34.你是否担心将会发生可怕的事情？',
'35.在结识新朋友时，你通常是主动的吗？',
'36.你觉得自己是个非常敏感的人吗？',
'37.和别人在一起的时候，你是否不常说话？',
'38.你是否认为结婚是个框框，应该废除？',
'39.你有时有点自吹自擂吗？',
'40.在一个沉闷的场合，你能给大家增添生气吗？',
'41.慢腾腾开车的司机是否使你讨厌？',
'42.你担心自己的健康吗？',
'43.你是否喜欢说笑话和谈论有趣的事情？',
'44.你是否觉得大多数事情对你都是无所谓的？',
'45.你小时候有过对父母鲁莽无礼的行为吗？',
'46.你喜欢和别人打成一片，整天相处在一起吗？',
'47.你失眠吗？',
'48.你饭前必定先洗手吗？',
'49.当别人问你话时，你是否对答如流？',
'50.你是否宁愿有富裕时间喜欢早点动身去赴约会？',
'51.你经常无缘无故感到疲倦和无精打采吗？',
'52.在游戏或打牌时你曾经作弊吗？',
'53.你喜欢紧张的工作吗？',
'54.你时常觉得自己的生活很单调吗？',
'55.你曾经为了自己而利用过别人吗？',
'56.你是否参加的活动太多，已超过自己可能分配的时间？',
'57.是否有那么几个人时常躲着你？',
'58.你是否认为人们为保障自己的将来而精打细算、勤俭节约所费的时间太多了？',
'59.你是否曾想过去死？',
'60.若你确知不会被发现时，你会少付给人家钱吗？',
'61.你能使一个联欢会开得成功吗？',
'62.你是否尽力使自己不粗鲁？',
'63.一件使你为难的事情过去之后，是否使你烦恼好久？',
'64.你曾否坚持要照你的想法去办事？',
'65.当你去乘火车时，你是否最后一分钟到达？',
'66.你是否容易紧张？',
'67.你常感到寂寞吗？',
'68.你的言行总是一致吗？',
'69.你有时喜欢玩弄动物吗？',
'70.有人对你或你的工作吹毛求疵时，是否容易伤害你的积极性？',
'71.你去赴约会或上班时，曾否迟到？',
'72.你是否喜欢在你的周围有许多热闹和高兴的事？',
'73.你愿意让别人怕你吗？',
'74.你是否有时兴致勃勃，有时却很懒散不想动弹？',
'75.你有时会把今天应该做的事拖到明天吗？',
'76.别人是否认为你是生气勃勃的？',
'77.别人是否对你说过许多慌话？',
'78.你是否对有些事情易性急生气？',
'79.若你犯有错误你是否愿意承认？',
'80.你是一个整洁严谨、有条不紊的人吗？',
'81.在公园里或马路上，你是否总是把果皮或废纸扔到垃圾箱里？',
'82.遇到为难的事情你是否拿不定主意？',
'83.你是否有过随口骂人的时候？',
'84.若你乘车或坐飞机外出时，你是否担心会碰撞或出意外？',
'85.你是一个爱交往的人吗？',
]

p_score = 0
e_score = 0
n_score = 0
l_score = 0


print('请回答以下题目，正确的输入1，错误的输入0,注意按回车结束输入：\n')

t = 0
while t < 85:
	print(theme[t] + '\n')
	result = raw_input("> ")
	# print(result)
	# print(type(result))

	if result != '1' and result != '0':
		print("输入错误请重新输入！\n")
		continue

	i = t + 1
	if i in P_RIGHT and result == '1':
		p_score += 1;
	if i in P_WRONG and result == '0':
		p_score += 1;

	if i in E_RIGHT and result == '1':
		e_score += 1;
	if i in E_WRONG and result == '0':
		e_score += 1;

	if i in N_RIGHT and result == '1':
		n_score += 1;
	if i in N_WRONG and result == '0':
		n_score += 1;

	if i in L_RIGHT and result == '1':
		l_score += 1;
	if i in L_WRONG and result == '0':
		l_score += 1;

	t += 1;

print('P分数：' + str(p_score))
print('E分数：' + str(e_score))
print('N分数：' + str(n_score))
print('L分数：' + str(l_score))






