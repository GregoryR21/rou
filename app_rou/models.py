from django.db import models

# Create your models here.
class Game(models.Model):
    counter = models.IntegerField(default=0)
    red = models.IntegerField(default=0)
    black = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    even_steve = models.IntegerField(default=0)
    odd_todd = models.IntegerField(default=0)
    _112 = models.IntegerField(default=0)
    _212 = models.IntegerField(default=0)
    _312 = models.IntegerField(default=0)
    _118 = models.IntegerField(default=0)
    _1936 = models.IntegerField(default=0)
    _col1 = models.IntegerField(default=0)
    _col2 = models.IntegerField(default=0)
    _col3 = models.IntegerField(default=0)
    _00 = models.IntegerField(default=0)
    _0 = models.IntegerField(default=0)
    _1 = models.IntegerField(default=0)
    _2 = models.IntegerField(default=0)
    _3 = models.IntegerField(default=0)
    _4 = models.IntegerField(default=0)
    _5 = models.IntegerField(default=0)
    _6 = models.IntegerField(default=0)
    _7 = models.IntegerField(default=0)
    _8 = models.IntegerField(default=0)
    _9 = models.IntegerField(default=0)
    _10 = models.IntegerField(default=0)
    _11 = models.IntegerField(default=0)
    _12 = models.IntegerField(default=0)
    _13 = models.IntegerField(default=0)
    _14 = models.IntegerField(default=0)
    _15 = models.IntegerField(default=0)
    _16 = models.IntegerField(default=0)
    _17 = models.IntegerField(default=0)
    _18 = models.IntegerField(default=0)
    _19 = models.IntegerField(default=0)
    _20 = models.IntegerField(default=0)
    _21 = models.IntegerField(default=0)
    _22 = models.IntegerField(default=0)
    _23 = models.IntegerField(default=0)
    _24 = models.IntegerField(default=0)
    _25 = models.IntegerField(default=0)
    _26 = models.IntegerField(default=0)
    _27 = models.IntegerField(default=0)
    _28 = models.IntegerField(default=0)
    _29 = models.IntegerField(default=0)
    _30 = models.IntegerField(default=0)
    _31 = models.IntegerField(default=0)
    _32 = models.IntegerField(default=0)
    _33 = models.IntegerField(default=0)
    _34 = models.IntegerField(default=0)
    _35 = models.IntegerField(default=0)
    _36 = models.IntegerField(default=0)
    _left = models.IntegerField(default=0)
    _right = models.IntegerField(default=0)
    _q1 = models.IntegerField(default=0)
    _q2 = models.IntegerField(default=0)
    _q3 = models.IntegerField(default=0)
    _q4 = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self): 
        return f"< id: {self.id} red : {self.red} black : {self.black} green : {self.green} even_steve : {self.even_steve} odd : {self.odd_todd} _112 : {self._112} _212 : {self._212} _312 : {self._312} _118 : {self._118} _1936 : {self._1936} _col1 : {self._col1} _col2 : {self._col2} _col3 : {self._col3} _00 : {self._00} _0 : {self._0} _1 : {self._1} _2 : {self._2} _3 : {self._3} _4 : {self._4} _5 : {self._5} _6 : {self._6} _7 : {self._7} _8 : {self._8} _9 : {self._9} _10 : {self._10} _11 : {self._11} _12 : {self._12} _13 : {self._13} _14 : {self._14} _15 : {self._15} _16 : {self._16} _17 : {self._17} _18 : {self._18} _19 : {self._19} _20 : {self._20} _21 : {self._21} _22 : {self._22} _23 : {self._23} _24 : {self._24} _25 : {self._25} _26 : {self._26} _27 : {self._27} _28 : {self._28} _29 : {self._29} _30 : {self._30} _31 : {self._31} _32 : {self._32} _33 : {self._33} _34 : {self._34} _35 : {self._35} _36 : {self._36} _left : {self._left} _right : {self._right} _q1 : {self._q1} _q2 : {self._q2} _q3 : {self._q3} _q4 : {self._q4}  >"