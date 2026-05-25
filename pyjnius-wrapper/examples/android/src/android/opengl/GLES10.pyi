from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES10:
    GL_ADD: ClassVar[int]
    GL_ALIASED_LINE_WIDTH_RANGE: ClassVar[int]
    GL_ALIASED_POINT_SIZE_RANGE: ClassVar[int]
    GL_ALPHA: ClassVar[int]
    GL_ALPHA_BITS: ClassVar[int]
    GL_ALPHA_TEST: ClassVar[int]
    GL_ALWAYS: ClassVar[int]
    GL_AMBIENT: ClassVar[int]
    GL_AMBIENT_AND_DIFFUSE: ClassVar[int]
    GL_AND: ClassVar[int]
    GL_AND_INVERTED: ClassVar[int]
    GL_AND_REVERSE: ClassVar[int]
    GL_BACK: ClassVar[int]
    GL_BLEND: ClassVar[int]
    GL_BLUE_BITS: ClassVar[int]
    GL_BYTE: ClassVar[int]
    GL_CCW: ClassVar[int]
    GL_CLAMP_TO_EDGE: ClassVar[int]
    GL_CLEAR: ClassVar[int]
    GL_COLOR_ARRAY: ClassVar[int]
    GL_COLOR_BUFFER_BIT: ClassVar[int]
    GL_COLOR_LOGIC_OP: ClassVar[int]
    GL_COLOR_MATERIAL: ClassVar[int]
    GL_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_CONSTANT_ATTENUATION: ClassVar[int]
    GL_COPY: ClassVar[int]
    GL_COPY_INVERTED: ClassVar[int]
    GL_CULL_FACE: ClassVar[int]
    GL_CW: ClassVar[int]
    GL_DECAL: ClassVar[int]
    GL_DECR: ClassVar[int]
    GL_DEPTH_BITS: ClassVar[int]
    GL_DEPTH_BUFFER_BIT: ClassVar[int]
    GL_DEPTH_TEST: ClassVar[int]
    GL_DIFFUSE: ClassVar[int]
    GL_DITHER: ClassVar[int]
    GL_DONT_CARE: ClassVar[int]
    GL_DST_ALPHA: ClassVar[int]
    GL_DST_COLOR: ClassVar[int]
    GL_EMISSION: ClassVar[int]
    GL_EQUAL: ClassVar[int]
    GL_EQUIV: ClassVar[int]
    GL_EXP: ClassVar[int]
    GL_EXP2: ClassVar[int]
    GL_EXTENSIONS: ClassVar[int]
    GL_FALSE: ClassVar[int]
    GL_FASTEST: ClassVar[int]
    GL_FIXED: ClassVar[int]
    GL_FLAT: ClassVar[int]
    GL_FLOAT: ClassVar[int]
    GL_FOG: ClassVar[int]
    GL_FOG_COLOR: ClassVar[int]
    GL_FOG_DENSITY: ClassVar[int]
    GL_FOG_END: ClassVar[int]
    GL_FOG_HINT: ClassVar[int]
    GL_FOG_MODE: ClassVar[int]
    GL_FOG_START: ClassVar[int]
    GL_FRONT: ClassVar[int]
    GL_FRONT_AND_BACK: ClassVar[int]
    GL_GEQUAL: ClassVar[int]
    GL_GREATER: ClassVar[int]
    GL_GREEN_BITS: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_TYPE_OES: ClassVar[int]
    GL_INCR: ClassVar[int]
    GL_INVALID_ENUM: ClassVar[int]
    GL_INVALID_OPERATION: ClassVar[int]
    GL_INVALID_VALUE: ClassVar[int]
    GL_INVERT: ClassVar[int]
    GL_KEEP: ClassVar[int]
    GL_LEQUAL: ClassVar[int]
    GL_LESS: ClassVar[int]
    GL_LIGHT0: ClassVar[int]
    GL_LIGHT1: ClassVar[int]
    GL_LIGHT2: ClassVar[int]
    GL_LIGHT3: ClassVar[int]
    GL_LIGHT4: ClassVar[int]
    GL_LIGHT5: ClassVar[int]
    GL_LIGHT6: ClassVar[int]
    GL_LIGHT7: ClassVar[int]
    GL_LIGHTING: ClassVar[int]
    GL_LIGHT_MODEL_AMBIENT: ClassVar[int]
    GL_LIGHT_MODEL_TWO_SIDE: ClassVar[int]
    GL_LINEAR: ClassVar[int]
    GL_LINEAR_ATTENUATION: ClassVar[int]
    GL_LINEAR_MIPMAP_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_NEAREST: ClassVar[int]
    GL_LINES: ClassVar[int]
    GL_LINE_LOOP: ClassVar[int]
    GL_LINE_SMOOTH: ClassVar[int]
    GL_LINE_SMOOTH_HINT: ClassVar[int]
    GL_LINE_STRIP: ClassVar[int]
    GL_LUMINANCE: ClassVar[int]
    GL_LUMINANCE_ALPHA: ClassVar[int]
    GL_MAX_ELEMENTS_INDICES: ClassVar[int]
    GL_MAX_ELEMENTS_VERTICES: ClassVar[int]
    GL_MAX_LIGHTS: ClassVar[int]
    GL_MAX_MODELVIEW_STACK_DEPTH: ClassVar[int]
    GL_MAX_PROJECTION_STACK_DEPTH: ClassVar[int]
    GL_MAX_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_TEXTURE_STACK_DEPTH: ClassVar[int]
    GL_MAX_TEXTURE_UNITS: ClassVar[int]
    GL_MAX_VIEWPORT_DIMS: ClassVar[int]
    GL_MODELVIEW: ClassVar[int]
    GL_MODULATE: ClassVar[int]
    GL_MULTISAMPLE: ClassVar[int]
    GL_NAND: ClassVar[int]
    GL_NEAREST: ClassVar[int]
    GL_NEAREST_MIPMAP_LINEAR: ClassVar[int]
    GL_NEAREST_MIPMAP_NEAREST: ClassVar[int]
    GL_NEVER: ClassVar[int]
    GL_NICEST: ClassVar[int]
    GL_NOOP: ClassVar[int]
    GL_NOR: ClassVar[int]
    GL_NORMALIZE: ClassVar[int]
    GL_NORMAL_ARRAY: ClassVar[int]
    GL_NOTEQUAL: ClassVar[int]
    GL_NO_ERROR: ClassVar[int]
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_ONE: ClassVar[int]
    GL_ONE_MINUS_DST_ALPHA: ClassVar[int]
    GL_ONE_MINUS_DST_COLOR: ClassVar[int]
    GL_ONE_MINUS_SRC_ALPHA: ClassVar[int]
    GL_ONE_MINUS_SRC_COLOR: ClassVar[int]
    GL_OR: ClassVar[int]
    GL_OR_INVERTED: ClassVar[int]
    GL_OR_REVERSE: ClassVar[int]
    GL_OUT_OF_MEMORY: ClassVar[int]
    GL_PACK_ALIGNMENT: ClassVar[int]
    GL_PALETTE4_R5_G6_B5_OES: ClassVar[int]
    GL_PALETTE4_RGB5_A1_OES: ClassVar[int]
    GL_PALETTE4_RGB8_OES: ClassVar[int]
    GL_PALETTE4_RGBA4_OES: ClassVar[int]
    GL_PALETTE4_RGBA8_OES: ClassVar[int]
    GL_PALETTE8_R5_G6_B5_OES: ClassVar[int]
    GL_PALETTE8_RGB5_A1_OES: ClassVar[int]
    GL_PALETTE8_RGB8_OES: ClassVar[int]
    GL_PALETTE8_RGBA4_OES: ClassVar[int]
    GL_PALETTE8_RGBA8_OES: ClassVar[int]
    GL_PERSPECTIVE_CORRECTION_HINT: ClassVar[int]
    GL_POINTS: ClassVar[int]
    GL_POINT_FADE_THRESHOLD_SIZE: ClassVar[int]
    GL_POINT_SIZE: ClassVar[int]
    GL_POINT_SMOOTH: ClassVar[int]
    GL_POINT_SMOOTH_HINT: ClassVar[int]
    GL_POLYGON_OFFSET_FILL: ClassVar[int]
    GL_POLYGON_SMOOTH_HINT: ClassVar[int]
    GL_POSITION: ClassVar[int]
    GL_PROJECTION: ClassVar[int]
    GL_QUADRATIC_ATTENUATION: ClassVar[int]
    GL_RED_BITS: ClassVar[int]
    GL_RENDERER: ClassVar[int]
    GL_REPEAT: ClassVar[int]
    GL_REPLACE: ClassVar[int]
    GL_RESCALE_NORMAL: ClassVar[int]
    GL_RGB: ClassVar[int]
    GL_RGBA: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_COVERAGE: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_ONE: ClassVar[int]
    GL_SAMPLE_COVERAGE: ClassVar[int]
    GL_SCISSOR_TEST: ClassVar[int]
    GL_SET: ClassVar[int]
    GL_SHININESS: ClassVar[int]
    GL_SHORT: ClassVar[int]
    GL_SMOOTH: ClassVar[int]
    GL_SMOOTH_LINE_WIDTH_RANGE: ClassVar[int]
    GL_SMOOTH_POINT_SIZE_RANGE: ClassVar[int]
    GL_SPECULAR: ClassVar[int]
    GL_SPOT_CUTOFF: ClassVar[int]
    GL_SPOT_DIRECTION: ClassVar[int]
    GL_SPOT_EXPONENT: ClassVar[int]
    GL_SRC_ALPHA: ClassVar[int]
    GL_SRC_ALPHA_SATURATE: ClassVar[int]
    GL_SRC_COLOR: ClassVar[int]
    GL_STACK_OVERFLOW: ClassVar[int]
    GL_STACK_UNDERFLOW: ClassVar[int]
    GL_STENCIL_BITS: ClassVar[int]
    GL_STENCIL_BUFFER_BIT: ClassVar[int]
    GL_STENCIL_TEST: ClassVar[int]
    GL_SUBPIXEL_BITS: ClassVar[int]
    GL_TEXTURE: ClassVar[int]
    GL_TEXTURE0: ClassVar[int]
    GL_TEXTURE1: ClassVar[int]
    GL_TEXTURE10: ClassVar[int]
    GL_TEXTURE11: ClassVar[int]
    GL_TEXTURE12: ClassVar[int]
    GL_TEXTURE13: ClassVar[int]
    GL_TEXTURE14: ClassVar[int]
    GL_TEXTURE15: ClassVar[int]
    GL_TEXTURE16: ClassVar[int]
    GL_TEXTURE17: ClassVar[int]
    GL_TEXTURE18: ClassVar[int]
    GL_TEXTURE19: ClassVar[int]
    GL_TEXTURE2: ClassVar[int]
    GL_TEXTURE20: ClassVar[int]
    GL_TEXTURE21: ClassVar[int]
    GL_TEXTURE22: ClassVar[int]
    GL_TEXTURE23: ClassVar[int]
    GL_TEXTURE24: ClassVar[int]
    GL_TEXTURE25: ClassVar[int]
    GL_TEXTURE26: ClassVar[int]
    GL_TEXTURE27: ClassVar[int]
    GL_TEXTURE28: ClassVar[int]
    GL_TEXTURE29: ClassVar[int]
    GL_TEXTURE3: ClassVar[int]
    GL_TEXTURE30: ClassVar[int]
    GL_TEXTURE31: ClassVar[int]
    GL_TEXTURE4: ClassVar[int]
    GL_TEXTURE5: ClassVar[int]
    GL_TEXTURE6: ClassVar[int]
    GL_TEXTURE7: ClassVar[int]
    GL_TEXTURE8: ClassVar[int]
    GL_TEXTURE9: ClassVar[int]
    GL_TEXTURE_2D: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY: ClassVar[int]
    GL_TEXTURE_ENV: ClassVar[int]
    GL_TEXTURE_ENV_COLOR: ClassVar[int]
    GL_TEXTURE_ENV_MODE: ClassVar[int]
    GL_TEXTURE_MAG_FILTER: ClassVar[int]
    GL_TEXTURE_MIN_FILTER: ClassVar[int]
    GL_TEXTURE_WRAP_S: ClassVar[int]
    GL_TEXTURE_WRAP_T: ClassVar[int]
    GL_TRIANGLES: ClassVar[int]
    GL_TRIANGLE_FAN: ClassVar[int]
    GL_TRIANGLE_STRIP: ClassVar[int]
    GL_TRUE: ClassVar[int]
    GL_UNPACK_ALIGNMENT: ClassVar[int]
    GL_UNSIGNED_BYTE: ClassVar[int]
    GL_UNSIGNED_SHORT: ClassVar[int]
    GL_UNSIGNED_SHORT_4_4_4_4: ClassVar[int]
    GL_UNSIGNED_SHORT_5_5_5_1: ClassVar[int]
    GL_UNSIGNED_SHORT_5_6_5: ClassVar[int]
    GL_VENDOR: ClassVar[int]
    GL_VERSION: ClassVar[int]
    GL_VERTEX_ARRAY: ClassVar[int]
    GL_XOR: ClassVar[int]
    GL_ZERO: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glActiveTexture(arg0: int) -> None: ...
    @staticmethod
    def glAlphaFunc(arg0: int, arg1: float) -> None: ...
    @staticmethod
    def glAlphaFuncx(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glBindTexture(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glBlendFunc(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glClear(arg0: int) -> None: ...
    @staticmethod
    def glClearColor(arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...
    @staticmethod
    def glClearColorx(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glClearDepthf(arg0: float) -> None: ...
    @staticmethod
    def glClearDepthx(arg0: int) -> None: ...
    @staticmethod
    def glClearStencil(arg0: int) -> None: ...
    @staticmethod
    def glClientActiveTexture(arg0: int) -> None: ...
    @staticmethod
    def glColor4f(arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...
    @staticmethod
    def glColor4x(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glColorMask(arg0: bool, arg1: bool, arg2: bool, arg3: bool) -> None: ...
    @staticmethod
    def glColorPointer(arg0: int, arg1: int, arg2: int, arg3: Buffer) -> None: ...
    @staticmethod
    def glCompressedTexImage2D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: Buffer) -> None: ...
    @staticmethod
    def glCompressedTexSubImage2D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: Buffer) -> None: ...
    @staticmethod
    def glCopyTexImage2D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None: ...
    @staticmethod
    def glCopyTexSubImage2D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None: ...
    @staticmethod
    def glCullFace(arg0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glDepthFunc(arg0: int) -> None: ...
    @staticmethod
    def glDepthMask(arg0: bool) -> None: ...
    @staticmethod
    def glDepthRangef(arg0: float, arg1: float) -> None: ...
    @staticmethod
    def glDepthRangex(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glDisable(arg0: int) -> None: ...
    @staticmethod
    def glDisableClientState(arg0: int) -> None: ...
    @staticmethod
    def glDrawArrays(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glDrawElements(arg0: int, arg1: int, arg2: int, arg3: Buffer) -> None: ...
    @staticmethod
    def glEnable(arg0: int) -> None: ...
    @staticmethod
    def glEnableClientState(arg0: int) -> None: ...
    @staticmethod
    def glFinish() -> None: ...
    @staticmethod
    def glFlush() -> None: ...
    @staticmethod
    def glFogf(arg0: int, arg1: float) -> None: ...
    @overload
    @staticmethod
    def glFogfv(arg0: int, arg1: list[float], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glFogfv(arg0: int, arg1: FloatBuffer) -> None: ...
    @staticmethod
    def glFogx(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glFogxv(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glFogxv(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glFrontFace(arg0: int) -> None: ...
    @staticmethod
    def glFrustumf(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> None: ...
    @staticmethod
    def glFrustumx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glGetError() -> int: ...
    @overload
    @staticmethod
    def glGetIntegerv(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetIntegerv(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glGetString(arg0: int) -> str: ...
    @staticmethod
    def glHint(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glLightModelf(arg0: int, arg1: float) -> None: ...
    @overload
    @staticmethod
    def glLightModelfv(arg0: int, arg1: list[float], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelfv(arg0: int, arg1: FloatBuffer) -> None: ...
    @staticmethod
    def glLightModelx(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxv(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxv(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glLightf(arg0: int, arg1: int, arg2: float) -> None: ...
    @overload
    @staticmethod
    def glLightfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glLightfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @staticmethod
    def glLightx(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glLightxv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glLightxv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glLineWidth(arg0: float) -> None: ...
    @staticmethod
    def glLineWidthx(arg0: int) -> None: ...
    @staticmethod
    def glLoadIdentity() -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixf(arg0: list[float], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixf(arg0: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixx(arg0: list[int], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixx(arg0: IntBuffer) -> None: ...
    @staticmethod
    def glLogicOp(arg0: int) -> None: ...
    @staticmethod
    def glMaterialf(arg0: int, arg1: int, arg2: float) -> None: ...
    @overload
    @staticmethod
    def glMaterialfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @staticmethod
    def glMaterialx(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glMatrixMode(arg0: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixf(arg0: list[float], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixf(arg0: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixx(arg0: list[int], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixx(arg0: IntBuffer) -> None: ...
    @staticmethod
    def glMultiTexCoord4f(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> None: ...
    @staticmethod
    def glMultiTexCoord4x(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glNormal3f(arg0: float, arg1: float, arg2: float) -> None: ...
    @staticmethod
    def glNormal3x(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glNormalPointer(arg0: int, arg1: int, arg2: Buffer) -> None: ...
    @staticmethod
    def glOrthof(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> None: ...
    @staticmethod
    def glOrthox(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    @staticmethod
    def glPixelStorei(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glPointSize(arg0: float) -> None: ...
    @staticmethod
    def glPointSizex(arg0: int) -> None: ...
    @staticmethod
    def glPolygonOffset(arg0: float, arg1: float) -> None: ...
    @staticmethod
    def glPolygonOffsetx(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glPopMatrix() -> None: ...
    @staticmethod
    def glPushMatrix() -> None: ...
    @staticmethod
    def glReadPixels(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: Buffer) -> None: ...
    @staticmethod
    def glRotatef(arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...
    @staticmethod
    def glRotatex(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glSampleCoverage(arg0: float, arg1: bool) -> None: ...
    @staticmethod
    def glSampleCoveragex(arg0: int, arg1: bool) -> None: ...
    @staticmethod
    def glScalef(arg0: float, arg1: float, arg2: float) -> None: ...
    @staticmethod
    def glScalex(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glScissor(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glShadeModel(arg0: int) -> None: ...
    @staticmethod
    def glStencilFunc(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glStencilMask(arg0: int) -> None: ...
    @staticmethod
    def glStencilOp(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glTexCoordPointer(arg0: int, arg1: int, arg2: int, arg3: Buffer) -> None: ...
    @staticmethod
    def glTexEnvf(arg0: int, arg1: int, arg2: float) -> None: ...
    @overload
    @staticmethod
    def glTexEnvfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @staticmethod
    def glTexEnvx(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glTexImage2D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: Buffer) -> None: ...
    @staticmethod
    def glTexParameterf(arg0: int, arg1: int, arg2: float) -> None: ...
    @staticmethod
    def glTexParameterx(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glTexSubImage2D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: Buffer) -> None: ...
    @staticmethod
    def glTranslatef(arg0: float, arg1: float, arg2: float) -> None: ...
    @staticmethod
    def glTranslatex(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glVertexPointer(arg0: int, arg1: int, arg2: int, arg3: Buffer) -> None: ...
    @staticmethod
    def glViewport(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
