from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JSONArray"]

class JSONArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/json/JSONArray"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Collection;)V", False), ("(Ljava/lang/Object;)V", False), ("(Lorg/json/JSONTokener;)V", False), ("(Ljava/lang/String;)V", False)]
    toJSONObject = JavaMethod("(Lorg/json/JSONArray;)Lorg/json/JSONObject;")
    optBoolean = JavaMultipleMethod([("(IZ)Z", False, False), ("(I)Z", False, False)])
    optDouble = JavaMultipleMethod([("(I)D", False, False), ("(ID)D", False, False)])
    optInt = JavaMultipleMethod([("(I)I", False, False), ("(II)I", False, False)])
    optJSONArray = JavaMethod("(I)Lorg/json/JSONArray;")
    optJSONObject = JavaMethod("(I)Lorg/json/JSONObject;")
    optLong = JavaMultipleMethod([("(I)J", False, False), ("(IJ)J", False, False)])
    optString = JavaMultipleMethod([("(ILjava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    getJSONArray = JavaMethod("(I)Lorg/json/JSONArray;")
    getJSONObject = JavaMethod("(I)Lorg/json/JSONObject;")
    remove = JavaMethod("(I)Ljava/lang/Object;")
    put = JavaMultipleMethod([("(IZ)Lorg/json/JSONArray;", False, False), ("(ID)Lorg/json/JSONArray;", False, False), ("(Z)Lorg/json/JSONArray;", False, False), ("(D)Lorg/json/JSONArray;", False, False), ("(I)Lorg/json/JSONArray;", False, False), ("(J)Lorg/json/JSONArray;", False, False), ("(Ljava/lang/Object;)Lorg/json/JSONArray;", False, False), ("(IJ)Lorg/json/JSONArray;", False, False), ("(II)Lorg/json/JSONArray;", False, False), ("(ILjava/lang/Object;)Lorg/json/JSONArray;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    length = JavaMethod("()I")
    toString = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    hashCode = JavaMethod("()I")
    getBoolean = JavaMethod("(I)Z")
    getInt = JavaMethod("(I)I")
    getLong = JavaMethod("(I)J")
    getDouble = JavaMethod("(I)D")
    get = JavaMethod("(I)Ljava/lang/Object;")
    join = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getString = JavaMethod("(I)Ljava/lang/String;")
    opt = JavaMethod("(I)Ljava/lang/Object;")
    isNull = JavaMethod("(I)Z")