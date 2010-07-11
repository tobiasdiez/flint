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

    Copyright (C) 2009 William Hart
    Copyright (C) 2010 Sebastian Pancratz

******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <mpir.h>
#include "flint.h"
#include "ulong_extras.h"
#include "fmpz.h"

int
main(void)
{
    int result;
    printf("sqrt....");
    fflush(stdout);

    fmpz_randinit();

    // Comparison with mpz routines
    for (ulong i = 0; i < 100000UL; i++)
    {
        fmpz_t f, g;
        mpz_t mf, mf2, mg;

        fmpz_init(f);
        fmpz_init(g);

        mpz_init(mf);
        mpz_init(mf2);
        mpz_init(mg);

        fmpz_randtest(g, 200);
        fmpz_abs(g, g);
        fmpz_get_mpz(mg, g);

        fmpz_sqrt(f, g);
        mpz_sqrt(mf, mg);

        fmpz_get_mpz(mf2, f);

        result = (mpz_cmp(mf2, mf) == 0);

        if (!result)
        {
            printf("FAIL\n");
            gmp_printf("mf = %Zd, mf2 = %Zd, mg = %Zd\n", mf, mf2, mg);
            abort();
        }

        fmpz_clear(f);
        fmpz_clear(g);

        mpz_clear(mf);
        mpz_clear(mf2);
        mpz_clear(mg);
    }

    // Check aliasing of f and g
    for (ulong i = 0; i < 100000UL; i++)
    {
        fmpz_t f;
        mpz_t mf, mf2;

        fmpz_init(f);

        mpz_init(mf);
        mpz_init(mf2);

        fmpz_randtest(f, 200);
        fmpz_abs(f, f);
        fmpz_get_mpz(mf, f);

        fmpz_sqrt(f, f);
        mpz_sqrt(mf, mf);

        fmpz_get_mpz(mf2, f);

        result = (mpz_cmp(mf, mf2) == 0);

        if (!result)
        {
            printf("FAIL\n");
            gmp_printf("mf = %Zd, mf2 = %Zd\n", mf, mf2);
            abort();
        }

        fmpz_clear(f);

        mpz_clear(mf);
        mpz_clear(mf2);
    }

    fmpz_randclear();

    _fmpz_cleanup();
    printf("PASS\n");
    return 0;
}
