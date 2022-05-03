# Encoding: UTF-8
from hybridmethods import hybridmethod, classmethod, instance


def test_hybridmethod():
    class Test:
        @hybridmethod
        def method(this):
            if instance(this):
                return "instance"
            else:
                return "class"

    inst_method = Test().method()
    cls_method = Test.method()

    assert inst_method == "instance"
    assert cls_method == "class"


def test_classmethod():
    class Test:
        @classmethod
        def method(cls, txt):
            print(txt)
            return "class"

        @method.instance
        def _(self, txt):
            print(txt)
            return "instance"

    inst_method = Test().method("Instance Method!")
    cls_method = Test.method("Class Method!")

    assert inst_method == "instance"
    assert cls_method == "class"
