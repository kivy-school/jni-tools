from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeTableProvider"]

class OSOutcomeTableProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/OSOutcomeTableProvider"
    __javaconstructor__ = [("()V", False)]
    upgradeOutcomeTableRevision1To2 = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    upgradeOutcomeTableRevision2To3 = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    upgradeCacheOutcomeTableRevision1To2 = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")