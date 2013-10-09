/*=============================================================================

    This file is part of FLINT.

    FLINT is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    FLINT is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with FLINT; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

=============================================================================*/
/******************************************************************************

    Copyright (C) 2013 Mike Hansen

******************************************************************************/
#include <stdio.h>
#include "fq_poly.h"

void
fq_poly_factor_print_pretty(const fq_poly_factor_t fac, const char *var,
                            const fq_ctx_t ctx)
{
    slong i;

    for (i = 0; i < fac->num; i++)
    {
        fq_poly_print_pretty(fac->poly + i, var, ctx);
        flint_printf(" ^ %ld\n", fac->exp[i]);
    }
}
