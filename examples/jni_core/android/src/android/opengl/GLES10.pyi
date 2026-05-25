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
    def glFogf(p0: int, p1: float) -> None: ...
    @staticmethod
    def glHint(p0: int, p1: int) -> None: ...
    @staticmethod
    def glFogx(p0: int, p1: int) -> None: ...
    @staticmethod
    def glActiveTexture(p0: int) -> None: ...
    @staticmethod
    def glAlphaFunc(p0: int, p1: float) -> None: ...
    @staticmethod
    def glAlphaFuncx(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindTexture(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFunc(p0: int, p1: int) -> None: ...
    @staticmethod
    def glClear(p0: int) -> None: ...
    @staticmethod
    def glClearColor(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glClearColorx(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glClearDepthf(p0: float) -> None: ...
    @staticmethod
    def glClearDepthx(p0: int) -> None: ...
    @staticmethod
    def glClearStencil(p0: int) -> None: ...
    @staticmethod
    def glClientActiveTexture(p0: int) -> None: ...
    @staticmethod
    def glColor4f(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glColor4x(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glColorMask(p0: bool, p1: bool, p2: bool, p3: bool) -> None: ...
    @staticmethod
    def glColorPointer(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glCompressedTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: Buffer) -> None: ...
    @staticmethod
    def glCompressedTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glCopyTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @staticmethod
    def glCopyTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @staticmethod
    def glCullFace(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glDepthFunc(p0: int) -> None: ...
    @staticmethod
    def glDepthMask(p0: bool) -> None: ...
    @staticmethod
    def glDepthRangef(p0: float, p1: float) -> None: ...
    @staticmethod
    def glDepthRangex(p0: int, p1: int) -> None: ...
    @staticmethod
    def glDisable(p0: int) -> None: ...
    @staticmethod
    def glDisableClientState(p0: int) -> None: ...
    @staticmethod
    def glDrawArrays(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glDrawElements(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glEnable(p0: int) -> None: ...
    @staticmethod
    def glEnableClientState(p0: int) -> None: ...
    @staticmethod
    def glFinish() -> None: ...
    @staticmethod
    def glFlush() -> None: ...
    @overload
    @staticmethod
    def glFogfv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glFogfv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glFogxv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glFogxv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glFrontFace(p0: int) -> None: ...
    @staticmethod
    def glFrustumf(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @staticmethod
    def glFrustumx(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGetError() -> int: ...
    @overload
    @staticmethod
    def glGetIntegerv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetIntegerv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGetString(p0: int) -> str: ...
    @staticmethod
    def glLightModelf(p0: int, p1: float) -> None: ...
    @overload
    @staticmethod
    def glLightModelfv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glLightModelfv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glLightModelx(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxv(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glLightf(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glLightfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glLightfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glLightx(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glLightxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glLightxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glLineWidth(p0: float) -> None: ...
    @staticmethod
    def glLineWidthx(p0: int) -> None: ...
    @staticmethod
    def glLoadIdentity() -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixf(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixf(p0: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixx(p0: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixx(p0: Any, p1: int) -> None: ...
    @staticmethod
    def glLogicOp(p0: int) -> None: ...
    @staticmethod
    def glMaterialf(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glMaterialfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glMaterialx(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glMatrixMode(p0: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixf(p0: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixf(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixx(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixx(p0: IntBuffer) -> None: ...
    @staticmethod
    def glMultiTexCoord4f(p0: int, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @staticmethod
    def glMultiTexCoord4x(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glNormal3f(p0: float, p1: float, p2: float) -> None: ...
    @staticmethod
    def glNormal3x(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glNormalPointer(p0: int, p1: int, p2: Buffer) -> None: ...
    @staticmethod
    def glOrthof(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @staticmethod
    def glOrthox(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @staticmethod
    def glPixelStorei(p0: int, p1: int) -> None: ...
    @staticmethod
    def glPointSize(p0: float) -> None: ...
    @staticmethod
    def glPointSizex(p0: int) -> None: ...
    @staticmethod
    def glPolygonOffset(p0: float, p1: float) -> None: ...
    @staticmethod
    def glPolygonOffsetx(p0: int, p1: int) -> None: ...
    @staticmethod
    def glPopMatrix() -> None: ...
    @staticmethod
    def glPushMatrix() -> None: ...
    @staticmethod
    def glReadPixels(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: Buffer) -> None: ...
    @staticmethod
    def glRotatef(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glRotatex(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glSampleCoverage(p0: float, p1: bool) -> None: ...
    @staticmethod
    def glSampleCoveragex(p0: int, p1: bool) -> None: ...
    @staticmethod
    def glScalef(p0: float, p1: float, p2: float) -> None: ...
    @staticmethod
    def glScalex(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glScissor(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glShadeModel(p0: int) -> None: ...
    @staticmethod
    def glStencilFunc(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glStencilMask(p0: int) -> None: ...
    @staticmethod
    def glStencilOp(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexCoordPointer(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glTexEnvf(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glTexEnvfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glTexEnvx(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glTexParameterf(p0: int, p1: int, p2: float) -> None: ...
    @staticmethod
    def glTexParameterx(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glTranslatef(p0: float, p1: float, p2: float) -> None: ...
    @staticmethod
    def glTranslatex(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glVertexPointer(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glViewport(p0: int, p1: int, p2: int, p3: int) -> None: ...
