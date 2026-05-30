from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class PropertyMapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/PropertyMapper"
    mapGravity = JavaMethod("(Ljava/lang/String;I)I")
    mapIntEnum = JavaMethod("(Ljava/lang/String;ILjava/util/function/IntFunction;)I")
    mapIntFlag = JavaMethod("(Ljava/lang/String;ILjava/util/function/IntFunction;)I")
    mapColor = JavaMethod("(Ljava/lang/String;I)I")
    mapDouble = JavaMethod("(Ljava/lang/String;I)I")
    mapFloat = JavaMethod("(Ljava/lang/String;I)I")
    mapLong = JavaMethod("(Ljava/lang/String;I)I")
    mapObject = JavaMethod("(Ljava/lang/String;I)I")
    mapResourceId = JavaMethod("(Ljava/lang/String;I)I")
    mapShort = JavaMethod("(Ljava/lang/String;I)I")
    mapBoolean = JavaMethod("(Ljava/lang/String;I)I")
    mapByte = JavaMethod("(Ljava/lang/String;I)I")
    mapInt = JavaMethod("(Ljava/lang/String;I)I")
    mapChar = JavaMethod("(Ljava/lang/String;I)I")

    class PropertyConflictException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inspector/PropertyMapper$PropertyConflictException"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]

class InspectionCompanion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/InspectionCompanion"
    mapProperties = JavaMethod("(Landroid/view/inspector/PropertyMapper;)V")
    readProperties = JavaMethod("(Ljava/lang/Object;Landroid/view/inspector/PropertyReader;)V")

    class UninitializedPropertyMapException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inspector/InspectionCompanion$UninitializedPropertyMapException"
        __javaconstructor__ = [("()V", False)]

class IntFlagMapping(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/IntFlagMapping"
    __javaconstructor__ = [("()V", False)]
    get = JavaMethod("(I)Ljava/util/Set;")
    add = JavaMethod("(IILjava/lang/String;)V")

class InspectionCompanionProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/InspectionCompanionProvider"
    provide = JavaMethod("(Ljava/lang/Class;)Landroid/view/inspector/InspectionCompanion;")

class StaticInspectionCompanionProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/StaticInspectionCompanionProvider"
    __javaconstructor__ = [("()V", False)]
    provide = JavaMethod("(Ljava/lang/Class;)Landroid/view/inspector/InspectionCompanion;")

class PropertyReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/PropertyReader"
    readColor = JavaMultipleMethod([("(ILandroid/graphics/Color;)V", False, False), ("(IJ)V", False, False), ("(II)V", False, False)])
    readGravity = JavaMethod("(II)V")
    readIntEnum = JavaMethod("(II)V")
    readIntFlag = JavaMethod("(II)V")
    readResourceId = JavaMethod("(II)V")
    readBoolean = JavaMethod("(IZ)V")
    readByte = JavaMethod("(IB)V")
    readShort = JavaMethod("(IS)V")
    readLong = JavaMethod("(IJ)V")
    readDouble = JavaMethod("(ID)V")
    readObject = JavaMethod("(ILjava/lang/Object;)V")
    readInt = JavaMethod("(II)V")
    readChar = JavaMethod("(IC)V")
    readFloat = JavaMethod("(IF)V")

    class PropertyTypeMismatchException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inspector/PropertyReader$PropertyTypeMismatchException"
        __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;)V", False), ("(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]

class WindowInspector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/WindowInspector"
    getGlobalWindowViews = JavaStaticMethod("()Ljava/util/List;")