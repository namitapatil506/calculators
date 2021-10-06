from django.contrib import messages
from django.shortcuts import render
from .unit import *
import math


def pulley_calculator(request):
    try:
        if request.method == 'POST':
            given_form1 = request.POST.get('given_form1')
            given_form2 = request.POST.get('given_form2')
            given_form3 = request.POST.get('given_form3')
            given_form4 = request.POST.get('given_form4')
            given_form5 = request.POST.get('given_form5')
            typec = Type()
            unit = Unit_conversion()

            if given_form1:
                t1 = request.POST.get('t1')
                v1 = request.POST.get('v1')
                p1 = request.POST.get('p1')
                t1_op = request.POST.get('t1_op')
                v1_op = request.POST.get('v1_op')
                p1_op = request.POST.get('p1_op')

                if given_form1 == 'form1':
                    context = {'given_form1': given_form1,'given_form2': 'form4','given_form3': 'form7',
                               'given_form4': 'form10','given_form5': 'form13'}
                    if v1 and p1 and t1 == None:
                        v1 = typec.type_conversion(v1)
                        p1 = typec.type_conversion(p1)

                        v1_new, text_v1 = unit.conversion('RPM', v1, v1_op)
                        p1_new, text_p1 = unit.conversion('W', p1, p1_op)

                        t1 = p1_new /(0.1046*v1_new)

                        context = {'p': '#drive-torque1', 'given_form1': given_form1,
                                   'given_form2': 'form4','given_form3': 'form7',
                               'given_form4': 'form10','given_form5': 'form13', 'v1': v1, 'p1': p1, 't1': t1,
                                   'v1_new': v1_new,'p1_new':p1_new,'v1_op': v1_op,'p1_op': p1_op,
                                   'text_v1': text_v1,'text_p1': text_p1}
                    return render(request, 'Physics/pulley-calculator.html', context)


                elif given_form1 == 'form2':
                    context = {'given_form1': given_form1,'given_form2': 'form4','given_form3': 'form7',
                               'given_form4': 'form10','given_form5': 'form13'}
                    if t1 and p1 and v1 == None:
                        t1 = typec.type_conversion(t1)
                        p1 = typec.type_conversion(p1)

                        t1_new, text_t1 = unit.conversion('Nm', t1, t1_op)
                        p1_new, text_p1 = unit.conversion('W', p1, p1_op)

                        v1 = p1_new / (0.1046 * t1_new)

                        context = {'p': '#angular-velocity1', 'given_form1': given_form1, 'given_form5': 'form13','v1': v1, 'p1': p1, 't1': t1,
                                   't1_new': t1_new, 'p1_new': p1_new, 't1_op': t1_op, 'p1_op': p1_op,'given_form2': 'form4','given_form3': 'form7',
                               'given_form4': 'form10',
                                   'text_t1': text_t1, 'text_p1': text_p1}
                    return render(request, 'Physics/pulley-calculator.html', context)


                elif given_form1 == 'form3':
                    context = {'given_form1': given_form1,'given_form2': 'form4','given_form3': 'form7',
                               'given_form4': 'form10','given_form5': 'form13'}
                    if t1 and v1 and p1 == None:
                        t1 = typec.type_conversion(t1)
                        v1 = typec.type_conversion(v1)

                        t1_new, text_t1 = unit.conversion('Nm', t1, t1_op)
                        v1_new, text_v1 = unit.conversion('RPM', v1, v1_op)

                        p1 = v1_new * (0.1046 * t1_new)

                        context = {'p': '#transmitting-power1', 'given_form1': given_form1,
                                   'given_form2': 'form4','given_form3': 'form7',
                               'given_form4': 'form10','given_form5': 'form13','v1': v1, 'p1': p1, 't1': t1,
                                   't1_new': t1_new, 'v1_new': v1_new, 't1_op': t1_op, 'v1_op': v1_op,
                                   'text_t1': text_t1, 'text_v1': text_v1}
                    return render(request, 'Physics/pulley-calculator.html', context)

            elif given_form2:
                t2 = request.POST.get('t2')
                v2 = request.POST.get('v2')
                p2 = request.POST.get('p2')
                t2_op = request.POST.get('t2_op')
                v2_op = request.POST.get('v2_op')
                p2_op = request.POST.get('p2_op')

                if given_form2 == 'form4':
                    context = {'given_form1': 'form1', 'given_form2': given_form2, 'given_form3': 'form7',
                               'given_form4': 'form10', 'given_form5': 'form13'}

                    if v2 and p2 and t2 == None:
                        v2 = typec.type_conversion(v2)
                        p2 = typec.type_conversion(p2)

                        v2_new, text_v2 = unit.conversion('RPM', v2, v2_op)
                        p2_new, text_p2 = unit.conversion('W', p2, p2_op)

                        t2 = p2_new / (0.1046 * v2_new)

                        context = {'p': '#drive-torque2', 'given_form2': given_form2,'given_form5': 'form13',
                                   'v2': v2, 'p2': p2, 't2': t2,'given_form1': 'form1','given_form3': 'form7',
                               'given_form4': 'form10',
                                   'v2_new': v2_new, 'p2_new': p2_new, 'v2_op': v2_op, 'p2_op': p2_op,
                                   'text_v2': text_v2, 'text_p2': text_p2}
                    return render(request, 'Physics/pulley-calculator.html', context)



                elif given_form2 == 'form5':
                    context = {'given_form1': 'form1', 'given_form2': given_form2, 'given_form3': 'form7',
                               'given_form4': 'form10', 'given_form5': 'form13'}

                    if t2 and p2 and v2 == None:
                        t2 = typec.type_conversion(t2)
                        p2 = typec.type_conversion(p2)

                        t2_new, text_t2 = unit.conversion('Nm', t2, t2_op)
                        p2_new, text_p2 = unit.conversion('W', p2, p2_op)

                        v2 = p2_new / (0.1046 * t2_new)

                        context = {'p': '#angular-velocity2', 'given_form2': given_form2,'given_form1': 'form1','given_form5': 'form13', 'v2': v2, 'p2': p2, 't2': t2,
                                   't2_new': t2_new, 'p2_new': p2_new, 't2_op': t2_op, 'p2_op': p2_op,'given_form3': 'form7',
                                   'given_form4': 'form10','text_t2': text_t2, 'text_p2': text_p2}
                    return render(request, 'Physics/pulley-calculator.html', context)



                elif given_form2 == 'form6':
                    context = {'given_form1': 'form1', 'given_form2': given_form2, 'given_form3': 'form7',
                               'given_form4': 'form10', 'given_form5': 'form13'}

                    if t2 and v2 and p2 == None:
                        t2 = typec.type_conversion(t2)
                        v2 = typec.type_conversion(v2)

                        t2_new, text_t2 = unit.conversion('Nm', t2, t2_op)
                        v2_new, text_v2 = unit.conversion('RPM', v2, v2_op)

                        p2 = v2_new * (0.1046 * t2_new)

                        context = {'p': '#transmitting-power2', 'given_form2': given_form2,'given_form5': 'form13', 'v2': v2, 'p2': p2, 't2': t2,
                                   't2_new': t2_new, 'v2_new': v2_new, 't2_op': t2_op, 'v2_op': v2_op,'given_form1': 'form1',
                                   'given_form3': 'form7','given_form4': 'form10','text_t2': text_t2, 'text_v2': text_v2}
                    return render(request, 'Physics/pulley-calculator.html', context)

            elif given_form3:
                v = request.POST.get('v')
                w = request.POST.get('w')
                d = request.POST.get('d')
                v_op = request.POST.get('v_op')
                w_op = request.POST.get('w_op')
                d_op = request.POST.get('d_op')


                if given_form3 == 'form7':
                    context = {'given_form1': 'form1', 'given_form2': 'form4', 'given_form3': given_form3,
                               'given_form4': 'form10', 'given_form5': 'form13'}

                    if w and d and v == None:
                        w = typec.type_conversion(w)
                        d = typec.type_conversion(d)
                        w_new, text_w = unit.conversion('RPM', w, w_op)
                        d_new, text_d = unit.conversion('m', d, d_op)

                        v=0.0523*d_new * w_new
                        context = {'p': '#belt-velocity', 'given_form3': given_form3, 'w': w, 'd': d, 'v': v,
                                   'w_new': w_new, 'd_new': d_new, 'w_op': w_op,'d_op': d_op,'text_w': text_w,'given_form1': 'form1',
                                    'given_form2': 'form4','given_form5': 'form13','given_form4': 'form10','text_d': text_d}

                    return render(request, 'Physics/pulley-calculator.html', context)


                elif given_form3 == 'form8':
                    context = {'given_form1': 'form1', 'given_form2': 'form4', 'given_form3': given_form3,
                               'given_form4': 'form10', 'given_form5': 'form13'}

                    if v and d and w == None:
                        v = typec.type_conversion(v)
                        d = typec.type_conversion(d)
                        v_new, text_v = unit.conversion('m/s', v, v_op)
                        d_new, text_d = unit.conversion('m', d, d_op)

                        w = v_new / (0.0523 * d_new)
                        context = {'p': '#angular-velocity3', 'given_form1': 'form1','given_form3': given_form3, 'w': w, 'd': d, 'v': v,
                                   'v_new': v_new, 'd_new': d_new, 'v_op': v_op, 'd_op': d_op, 'text_v': text_v,'given_form4': 'form10', 'given_form5': 'form13',
                                   'given_form2': 'form4','text_d': text_d}

                    return render(request, 'Physics/pulley-calculator.html', context)


                elif given_form3 == 'form9':
                    context = {'given_form1': 'form1', 'given_form2': 'form4', 'given_form3': given_form3,
                               'given_form4': 'form10', 'given_form5': 'form13'}

                    if v and w and d == None:
                        v = typec.type_conversion(v)
                        w = typec.type_conversion(w)
                        v_new, text_v = unit.conversion('m/s', v, v_op)
                        w_new, text_w = unit.conversion('RPM', w, w_op)

                        d = v_new / (0.0523 * w_new)

                        context = {'p': '#diameter', 'given_form3': given_form3,'given_form5': 'form13', 'w': w, 'd': d, 'v': v,
                                   'v_new': v_new, 'w_new': w_new, 'w_op': w_op, 'v_op': v_op, 'text_v': text_v,'given_form1': 'form1',
                                   'given_form2': 'form4','given_form4': 'form10','text_w': text_w}

                    return render(request, 'Physics/pulley-calculator.html', context)

            elif given_form4:
                bt = request.POST.get('bt')
                p4 = request.POST.get('p4')
                v4 = request.POST.get('v4')
                bt_op = request.POST.get('bt_op')
                p4_op = request.POST.get('p4_op')
                v4_op = request.POST.get('v4_op')


                if given_form4 == 'form10':
                    context = {'given_form1': 'form1', 'given_form2': 'form4', 'given_form3': 'form7',
                               'given_form4': given_form4, 'given_form5': 'form13'}

                    if p4 and v4 and bt == None:
                        p4 = typec.type_conversion(p4)
                        v4 = typec.type_conversion(v4)
                        p4_new, text_p4 = unit.conversion('W', p4, p4_op)
                        v4_new, text_v4 = unit.conversion('m/s', v4, v4_op)

                        bt=p4_new/v4_new
                        context = {'p': '#belt-tension', 'given_form4': given_form4,'given_form5': 'form13', 'p4': p4, 'bt': bt, 'v4': v4,
                                   'p4_new': p4_new, 'v4_new': v4_new, 'p4_op': p4_op,'v4_op': v4_op,'text_p4': text_p4,'given_form1': 'form1',
                                   'given_form2': 'form4','given_form3': 'form7','text_v4': text_v4}

                    return render(request, 'Physics/pulley-calculator.html', context)

                if given_form4 == 'form11':
                    context = {'given_form1': 'form1', 'given_form2': 'form4', 'given_form3': 'form7',
                               'given_form4': given_form4, 'given_form5': 'form13'}

                    if bt and v4 and p4 == None:
                        bt = typec.type_conversion(bt)
                        v4 = typec.type_conversion(v4)
                        bt_new, text_bt = unit.conversion('N', bt, bt_op)
                        v4_new, text_v4 = unit.conversion('m/s', v4, v4_op)

                        p4 = bt_new * v4_new

                        context = {'p': '#transmitting-power4', 'given_form4': given_form4,'given_form5': 'form13', 'p4': p4, 'bt': bt, 'v4': v4,
                                   'bt_new': bt_new, 'v4_new': v4_new, 'bt_op': bt_op, 'v4_op': v4_op,'text_bt': text_bt,'given_form1': 'form1',
                                   'given_form2': 'form4','given_form3': 'form7','text_v4': text_v4}

                    return render(request, 'Physics/pulley-calculator.html', context)

                if given_form4 == 'form12':

                    context = {'given_form1': 'form1', 'given_form2': 'form4', 'given_form3': 'form7',
                               'given_form4': given_form4, 'given_form5': 'form13'}

                    if bt and p4 and v4 == None:
                        bt = typec.type_conversion(bt)
                        p4 = typec.type_conversion(p4)
                        bt_new, text_bt = unit.conversion('N', bt, bt_op)
                        p4_new, text_p4 = unit.conversion('W', p4, p4_op)

                        v4 = p4_new / bt_new

                        context = {'p': '#belt-velocity4', 'given_form4': given_form4,'given_form5': 'form13', 'p4': p4, 'bt': bt, 'v4': v4,
                                   'bt_new': bt_new, 'p4_new': p4_new, 'bt_op': bt_op, 'p4_op': p4_op,'text_bt': text_bt,'given_form1': 'form1',
                                   'text_p4': text_p4,'given_form2': 'form4', 'given_form3': 'form7',}

                    return render(request, 'Physics/pulley-calculator.html', context)

            elif given_form5:
                d1 = request.POST.get('d1')
                d2 = request.POST.get('d2')
                D = request.POST.get('D')
                L = request.POST.get('L')
                d1_op = request.POST.get('d1_op')
                d2_op = request.POST.get('d2_op')
                D_op = request.POST.get('D_op')


                if given_form5 == 'form13':
                    context = {'given_form1': 'form1', 'given_form2': 'form4', 'given_form3': 'form7',
                               'given_form4': 'form10', 'given_form5': 'form13'}

                    if d1 and d2 and D and L== None:
                        d1 = typec.type_conversion(d1)
                        d2 = typec.type_conversion(d2)
                        D = typec.type_conversion(D)
                        d1_new, text_d1 = unit.conversion('m', d1, d1_op)
                        d2_new, text_d2 = unit.conversion('m', d2, d2_op)
                        D_new, text_D = unit.conversion('m', D, D_op)

                        L = (d1_new * 1.57) + (d2_new * 1.57) + 2*D_new + ((d1_new - d2_new)**2 / 4*D_new)
                        context = {'p': '#belt-length', 'given_form5': given_form5, 'd1': d1, 'd2': d2, 'D': D,'L':L,
                                   'd1_new': d1_new, 'd2_new': d2_new,'D_new': D_new, 'd1_op': d1_op,'d2_op': d2_op,
                                   'D_op': D_op,'text_d1': text_d1,'text_d2': text_d2,'text_D': text_D,'given_form1': 'form1', 'given_form2': 'form4', 'given_form3': 'form7',
                               'given_form4': 'form10'}

                    return render(request,'Physics/pulley-calculator.html',context)



    except Exception as e:
        print(e)
    return render(request, 'Physics/pulley-calculator.html', {'given_form1': 'form1','given_form2': 'form4',
                                                              'given_form3': 'form7','given_form4': 'form10',
                                                              'given_form5': 'form13'})