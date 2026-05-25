from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JSONArray"]

class JSONArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/json/JSONArray"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Collection;)V", False), ("(Lorg/json/JSONTokener;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Object;)V", False)]
    length = JavaMethod("()I")
    put = JavaMultipleMethod([("(Z)Lorg/json/JSONArray;", False, False), ("(D)Lorg/json/JSONArray;", False, False), ("(I)Lorg/json/JSONArray;", False, False), ("(J)Lorg/json/JSONArray;", False, False), ("(Ljava/lang/Object;)Lorg/json/JSONArray;", False, False), ("(IZ)Lorg/json/JSONArray;", False, False), ("(ID)Lorg/json/JSONArray;", False, False), ("(II)Lorg/json/JSONArray;", False, False), ("(IJ)Lorg/json/JSONArray;", False, False), ("(ILjava/lang/Object;)Lorg/json/JSONArray;", False, False)])
    isNull = JavaMethod("(I)Z")
    get = JavaMethod("(I)Ljava/lang/Object;")
    opt = JavaMethod("(I)Ljava/lang/Object;")
    remove = JavaMethod("(I)Ljava/lang/Object;")
    getBoolean = JavaMethod("(I)Z")
    optBoolean = JavaMultipleMethod([("(I)Z", False, False), ("(IZ)Z", False, False)])
    getDouble = JavaMethod("(I)D")
    optDouble = JavaMultipleMethod([("(I)D", False, False), ("(ID)D", False, False)])
    getInt = JavaMethod("(I)I")
    optInt = JavaMultipleMethod([("(I)I", False, False), ("(II)I", False, False)])
    getLong = JavaMethod("(I)J")
    optLong = JavaMultipleMethod([("(I)J", False, False), ("(IJ)J", False, False)])
    getString = JavaMethod("(I)Ljava/lang/String;")
    optString = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(ILjava/lang/String;)Ljava/lang/String;", False, False)])
    getJSONArray = JavaMethod("(I)Lorg/json/JSONArray;")
    optJSONArray = JavaMethod("(I)Lorg/json/JSONArray;")
    getJSONObject = JavaMethod("(I)Lorg/json/JSONObject;")
    optJSONObject = JavaMethod("(I)Lorg/json/JSONObject;")
    toJSONObject = JavaMethod("(Lorg/json/JSONArray;)Lorg/json/JSONObject;")
    join = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    toString = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")